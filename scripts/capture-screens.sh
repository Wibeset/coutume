#!/bin/sh
# Captures the row of screens from the iOS app in the simulator, with its sample habits,
# and writes them as AVIF + WebP to assets/screens/<lang>/.
#
#   scripts/capture-screens.sh fr      # or: en, es
#
# Needs Xcode, ../coutume-ios, and cwebp + avifenc (brew install webp libavif).
set -eu

LANG_CODE=${1:?usage: $0 fr|en|es}
case "$LANG_CODE" in
  fr) LOCALE=fr_CA ;;
  en) LOCALE=en_CA ;;
  es) LOCALE=es_MX ;;
  *) echo "unknown language: $LANG_CODE" >&2; exit 1 ;;
esac

SITE=$(cd "$(dirname "$0")/.." && pwd)
IOS=${IOS_REPO:-$SITE/../coutume-ios}
# A simulator name or UDID; a UDID keeps the capture off a simulator you're using.
DEVICE=${DEVICE:-iPhone 17 Pro}
UDID_PATTERN='[0-9A-F]{8}(-[0-9A-F]{4}){3}-[0-9A-F]{12}'
if echo "$DEVICE" | grep -qxE "$UDID_PATTERN"; then
  UDID=$DEVICE
else
  # "Name (" so « iPhone 17 Pro » doesn't pick « iPhone 17 Pro Max ».
  UDID=$(xcrun simctl list devices available | grep -F "    $DEVICE (" | grep -m1 -oE "$UDID_PATTERN")
fi
BUNDLE=ca.wibeset.Coutume
OUT=$SITE/assets/screens/$LANG_CODE
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# Unsigned: the simulator doesn't need a team, and the sample data lives in memory.
xcodebuild -project "$IOS/Coutume.xcodeproj" -scheme Coutume -configuration Debug \
  -destination "platform=iOS Simulator,id=$UDID" -derivedDataPath "$IOS/build" build -quiet CODE_SIGNING_ALLOWED=NO
xcrun simctl boot "$UDID" 2>/dev/null || true
xcrun simctl bootstatus "$UDID" >/dev/null
xcrun simctl install "$UDID" "$IOS/build/Build/Products/Debug-iphonesimulator/Coutume.app"
xcrun simctl status_bar "$UDID" override --time 9:41 --dataNetwork wifi --wifiMode active \
  --wifiBars 3 --cellularMode active --cellularBars 4 --batteryState charged --batteryLevel 100
trap 'xcrun simctl status_bar "$UDID" clear; rm -rf "$TMP"' EXIT

mkdir -p "$OUT"
# Site name → app debug screen ("" is the day, which the app opens on), the row of phones on the home page.
# SCREENS="today:" recaptures only some (the -debugScreen names are listed in coutume-ios's README).
SCREENS=${SCREENS:-"today: detail:detail quit:quit progress:milestones calendar:calendar"}
# The site is on ink, so the app is captured dark; APPEARANCES="dark light" captures both
# (the light ones get a -light suffix).
APPEARANCES=${APPEARANCES:-dark}
for pair in $SCREENS; do
  name=${pair%%:*} screen=${pair#*:}
  for appearance in $APPEARANCES; do
    suffix=$([ "$appearance" = light ] && echo -light || true)
    xcrun simctl terminate "$UDID" "$BUNDLE" 2>/dev/null || true
    xcrun simctl launch "$UDID" "$BUNDLE" -seedSampleData -inMemoryStore -sampleHealth -appearance "$appearance" \
      -AppleLanguages "($LANG_CODE)" -AppleLocale "$LOCALE" ${screen:+-debugScreen "$screen"} >/dev/null
    sleep 5
    xcrun simctl io "$UDID" screenshot "$TMP/raw.png" >/dev/null 2>&1
    # 750 px wide covers the phone frame at 2x.
    sips -s format png --resampleWidth 750 "$TMP/raw.png" --out "$TMP/shot.png" >/dev/null
    cwebp -quiet -q 80 -m 6 -sharp_yuv "$TMP/shot.png" -o "$OUT/$name$suffix.webp"
    avifenc -q 60 -s 4 "$TMP/shot.png" "$OUT/$name$suffix.avif" >/dev/null
    echo "$OUT/$name$suffix"
  done
done
xcrun simctl terminate "$UDID" "$BUNDLE" 2>/dev/null || true
