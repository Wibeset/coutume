# The guides of coutume.app, in Spanish. Same structure and markup as the `en` dicts in content.py.

from alternatives import ALT_ES

SCREENS_ES = {
    "today": "El día: seis hábitos, cada uno con su anillo",
    "detail": "10.000 pasos, completados por Salud, con su racha y su historial",
    "quit": "Un hábito por dejar: 12 días sin bebidas energéticas, 42 $ ahorrados",
    "progress": "Progreso: el nivel alcanzado y los logros conseguidos",
    "calendar": "El calendario: el mes, más brillante cuantos más hábitos se cumplieron",
}

ES = {
# ---------------------------------------------------------------- Alternatives (alternatives.py)
**ALT_ES,

# ---------------------------------------------------------------- Features and uses
"health": dict(
  slug="seguimiento-habitos-salud",
  title="Seguimiento de hábitos con Salud: pasos y agua, solos — Coutume",
  desc="Coutume sigue tus hábitos en iPhone y lee Salud: pasos, ejercicio, atención plena y agua completan tus hábitos solos. Gratis, solo lectura, sin cuenta.",
  crumb="Seguimiento de hábitos con Salud", guide="Pasos, ejercicio, minutos de atención plena y agua, completados por Salud",
  h1="Una app de hábitos que Salud completa por ti",
  lede="Camina, y tu hábito de pasos se llena solo. Coutume lee cuatro tipos de datos de Salud para registrar tus hábitos por su cuenta, así que solo tocas para el resto. Gratis, sin cuenta y sin anuncios.",
  sections=[
    ("detail", "Cuatro hábitos que se registran solos", "<p>Pasos, minutos de ejercicio, minutos de atención plena y agua. Vincula un hábito a uno de ellos, como 10.000 pasos u 8 vasos de agua, y su anillo se llena a medida que Salud cuenta.</p>"),
    ("detail", "El mismo total que la app Salud", "<p>Coutume usa el mismo total diario que Salud, que cuenta tu iPhone y tu Apple Watch una sola vez. Los datos del Apple Watch pueden llegar a tu iPhone un poco más tarde: cada vez que abres Coutume, vuelve a leer los últimos siete días y se pone al día.</p>"),
    ("today", "Junto a los hábitos que tocas", "<p>Tus hábitos de Salud conviven con los demás en tu día: leer 20 páginas, meditar, acostarte a tu hora. Un toque registra esos; Salud registra el resto.</p>"),
    ("calendar", "Solo lectura, y privado", "<p>Coutume nunca escribe en Salud, y nunca lee nada que no hayas permitido. Los totales diarios se quedan en tu iPhone y en tu iCloud privado: nunca nos llegan ni se usan para publicidad. Puedes cambiar lo que lee Coutume cuando quieras en Ajustes › Privacidad y seguridad › Salud › Coutume.</p>"),
  ]),

"energy": dict(
  slug="dejar-bebidas-energeticas",
  title="Dejar las bebidas energéticas: cuenta tus días sin — Coutume",
  desc="¿Quieres dejar las bebidas energéticas? Coutume cuenta tus días sin, el dinero que ahorras y los impulsos que resistes, en iPhone. Gratis, privada y sin cuenta.",
  crumb="Dejar las bebidas energéticas", guide="Cuenta tus días sin bebidas energéticas y el dinero que ahorras",
  h1="Dejar las bebidas energéticas, un día a la vez",
  lede="Coutume es una app de hábitos gratis para iPhone con un tipo de hábito pensado para dejar: cuenta tus días sin bebidas energéticas, el dinero que ahorras y los impulsos que resistes. Sin cuenta, sin anuncios.",
  sections=[
    ("quit", "Cumplido por defecto, registrado solo si recaes", "<p>La mayoría de las apps quieren que marques una casilla cada día. Un hábito por dejar funciona al revés: cada día cuenta como cumplido, salvo que registres una recaída. En un buen día, no tienes nada que hacer.</p>"),
    ("quit", "Días sin, dinero ahorrado, impulsos resistidos", "<p>Coutume cuenta tus días sin bebidas energéticas, el dinero que no gastaste en latas y los impulsos que resististe, para que los veas sumar semana tras semana.</p>"),
    ("progress", "Una recaída reinicia la cuenta, no todo lo demás", "<p>Si recaes, la cuenta de días sin vuelve a empezar. Tu nivel, tus logros y tu mes se quedan: cuentan cada día que cumpliste.</p>"),
    ("today", "Reemplázalas por otra cosa", "<p>Dejar algo es más fácil con otra cosa en su lugar. Añade al lado un hábito por crear, como 8 vasos de agua o una caminata, y llena su anillo con un toque, o deja que Salud lo llene por ti.</p>"),
  ],
  extra="<p class=\"note\">Coutume es una app de hábitos, no una app médica. Si te preocupa cuánta cafeína tomas, habla con un médico o un farmacéutico.</p>"),

"vaping": dict(
  slug="dejar-de-vapear",
  title="App para dejar de vapear: días sin y dinero ahorrado — Coutume",
  desc="Una app gratis para dejar de vapear en iPhone: Coutume cuenta tus días sin vapear, el dinero que ahorras y los impulsos que resistes. Sin cuenta.",
  crumb="Dejar de vapear", guide="Sigue tus días sin vapear, el dinero ahorrado y los impulsos resistidos",
  h1="Dejar de vapear, contando lo que ganas",
  lede="Crea “Sin vapear” como hábito por dejar, y Coutume cuenta cada día sin vapear, el dinero que ahorras y los impulsos que superas. Gratis, privada, en iPhone.",
  sections=[
    ("quit", "Nada que registrar en un buen día", "<p>Un hábito por dejar se da por cumplido. No marcas nada cuando no vapeaste; solo registras el día que recaes. Coutume cuenta por ti.</p>"),
    ("quit", "Mira cómo crecen los días y el ahorro", "<p>Tus días sin vapear, el dinero que no gastaste y los impulsos que resististe esta semana, uno al lado del otro en la página del hábito.</p>"),
    ("progress", "Cada día cumplido sigue contando", "<p>Una recaída reinicia la cuenta de días sin, pero nunca te quita tu nivel ni tus logros. Quince niveles y dieciocho logros marcan el camino, un día cumplido tras otro.</p>"),
    ("calendar", "Mira tu mes", "<p>El calendario muestra cada día del mes, más brillante cuantos más hábitos cumpliste: una forma tranquila de ver todo lo que has avanzado.</p>"),
  ],
  extra="<p class=\"note\">Coutume es una app de hábitos, no una app médica ni un programa para dejar de fumar. Para recibir ayuda para dejar de vapear, habla con un médico, un farmacéutico o una línea de ayuda local para dejar de fumar.</p>"),

"dayswithout": dict(
  slug="contador-dias-sin",
  title="Contador de días sin para iPhone: cualquier hábito que dejes — Coutume",
  desc="Un contador de “días sin” gratis para iPhone: azúcar, café, redes sociales. Coutume cuenta tus días sin, el dinero ahorrado y los impulsos resistidos.",
  crumb="Contador de días sin", guide="Un contador de días sin para todo lo que quieras dejar",
  h1="Un contador de “días sin” para todo lo que dejas",
  lede="El azúcar, el café, las redes de madrugada, las bebidas energéticas: ponle nombre a lo que quieres dejar, y Coutume cuenta tus días sin. Una app de hábitos gratis para iPhone, sin cuenta y sin anuncios.",
  sections=[
    ("quit", "Cualquier hábito que quieras dejar", "<p>Crea un hábito por dejar y dale un nombre y un icono. A partir de ahí, cada día cuenta como cumplido salvo que registres una recaída, y la cuenta de días sin crece sola.</p>"),
    ("quit", "Más que un número de días", "<p>Coutume también cuenta el dinero que ahorras y los impulsos que resistes, así que una tarde difícil que superaste cuenta para algo.</p>"),
    ("progress", "Una recaída no es el final", "<p>Una recaída reinicia la cuenta, nunca tu mes ni tu nivel. Tus logros siguen ganados, y cada día cumplido sigue contando.</p>"),
    ("calendar", "Varios a la vez", "<p>Deja más de una cosa, y crea buenos hábitos al lado: todos comparten tu día, tu calendario y tus niveles.</p>"),
  ]),

"water": dict(
  slug="seguimiento-agua",
  title="Seguimiento de agua en iPhone: 8 vasos al día, con un toque — Coutume",
  desc="Sigue el agua que bebes en iPhone: toca un anillo por cada vaso, o deja que Salud lo complete. Gratis, con rachas y niveles, sin cuenta.",
  crumb="Seguimiento de agua", guide="Cuenta tus vasos de agua con un toque, o deja que Salud lo haga",
  h1="Seguir tu agua, un toque por vaso",
  lede="Fija un objetivo diario, como 8 vasos de agua, y toca el anillo cada vez que bebas. O deja que Salud lo complete. Coutume es una app de hábitos gratis para iPhone, sin cuenta y sin anuncios.",
  sections=[
    ("today", "Un toque, un vaso", "<p>Un hábito que se cuenta suma uno con cada toque, y su anillo se llena hacia tu objetivo. Mantén pulsado el anillo para escribir un número o deshacer el último vaso.</p>"),
    ("detail", "O deja que Salud cuente", "<p>Si ya registras tu agua en Salud, o con una app o una botella que escribe en ella, vincula tu hábito de agua a Salud y se completará solo.</p>"),
    ("calendar", "Una racha que perdona", "<p>Cada día que alcanzas tu objetivo alarga tu racha, y se perdona un día perdido por semana. El calendario muestra tu mes, más brillante cuantos más hábitos se cumplieron.</p>"),
    ("today", "Con tus otros hábitos", "<p>El agua convive con tus pasos, tu lectura o tu hora de dormir, en el mismo día y en el mismo widget de la pantalla de inicio.</p>"),
  ]),

"free": dict(
  slug="app-habitos-gratis",
  title="App de hábitos gratis para iPhone: sin cuenta ni anuncios — Coutume",
  desc="Una app de hábitos realmente gratis para iPhone: sin suscripción, sin anuncios, sin cuenta ni límite. Hábitos por crear y por dejar, Salud y widgets.",
  crumb="App de hábitos gratis", guide="Gratis de verdad: sin suscripción, sin anuncios, sin cuenta",
  h1="Una app de hábitos gratis de verdad",
  lede="Sin prueba que se acaba, sin un cuarto hábito tras un pago, sin anuncios entre tus anillos. Coutume es una app de hábitos gratis para iPhone, sin cuenta y sin suscripción.",
  sections=[
    ("today", "Todo, gratis", "<p>Hábitos por crear y por dejar, Salud, rachas que perdonan, niveles, logros, el calendario, widgets y sincronización con iCloud: todo, sin plan de pago.</p>"),
    ("quit", "Sin cuenta que crear", "<p>Abre la app y añade tu primer hábito. Sin registro, sin correo electrónico y sin contraseña, y nada que borrar después.</p>"),
    ("progress", "Sin anuncios, sin rastreo", "<p>Coutume no tiene anuncios, ni analíticas, ni servidor propio. Tus hábitos se quedan en tu iPhone y en tu iCloud privado, y nunca los recibimos.</p>"),
    ("calendar", "Por qué es gratis", "<p>Coutume la hace Wibeset, un pequeño estudio en Canadá que crea las apps que quiere usar, como Reliure para la lectura. Es gratis porque una app de hábitos no debería costarte una suscripción.</p>"),
  ]),

"widget": dict(
  slug="widget-habitos",
  title="Widget de hábitos: tus anillos en la pantalla de inicio — Coutume",
  desc="Mira tus hábitos sin abrir la app: los widgets de Coutume muestran los anillos del día y tu racha en la pantalla de inicio y la pantalla bloqueada.",
  crumb="Widget de hábitos", guide="Los anillos del día en tu pantalla de inicio y tu pantalla bloqueada",
  h1="Tus hábitos, directamente en tu pantalla de inicio",
  lede="Los widgets de Coutume muestran los anillos del día y tu racha de días perfectos en tu pantalla de inicio, y también caben en la pantalla bloqueada. Una app de hábitos gratis para iPhone, sin cuenta y sin anuncios.",
  sections=[
    ("today", "Tu día de un vistazo", "<p>El anillo de cada hábito, tan lleno como tu día: los vasos de agua, los pasos que completa Salud, los hábitos que dejas, cumplidos por defecto.</p>"),
    ("calendar", "Tu racha de días perfectos", "<p>El widget también muestra cuántos días perfectos seguidos llevas, esos en los que cumpliste todos tus hábitos.</p>"),
    ("today", "Añadir el widget", "<p>Mantén pulsada la pantalla de inicio, toca <strong>Editar</strong> › <strong>Añadir widget</strong> y elige Coutume. En la pantalla bloqueada, mantenla pulsada, toca <strong>Personalizar</strong> y añade Coutume a los widgets bajo la hora.</p>"),
  ]),

# ---------------------------------------------------------------- Articles
"ideas": dict(
  slug="ideas-habitos",
  title="40 ideas de hábitos: buenos por crear y malos por dejar — Coutume",
  desc="40 ideas de buenos hábitos por crear y malos por dejar, para la salud, el sueño, la mente y el dinero, con consejos para mantener cada uno.",
  crumb="Ideas de hábitos", guide="40 ideas de buenos hábitos por crear y malos por dejar",
  h1="40 ideas de hábitos, por crear y por dejar",
  lede="¿No sabes qué hábitos seguir? Aquí tienes cuarenta ideas, ordenadas por tema. Elige dos o tres, no diez: los hábitos pequeños que mantienes valen más que los grandes que abandonas.",
  body="""
      <h2>Salud y movimiento</h2>
      <ul>
        <li><strong>Beber 8 vasos de agua.</strong> Cuéntalos con un toque cada uno, o deja que Salud los complete.</li>
        <li><strong>Caminar 10.000 pasos</strong>, o 6000 para empezar: un objetivo que alcanzas casi todos los días mantiene viva la racha.</li>
        <li><strong>Moverte 30 minutos.</strong> Salud cuenta tus minutos de ejercicio.</li>
        <li><strong>Estirarte 5 minutos</strong> al despertar.</li>
        <li><strong>Comer una fruta o una verdura</strong> en cada comida.</li>
        <li><strong>Subir por las escaleras.</strong></li>
        <li><strong>Cocinar la cena en casa.</strong></li>
        <li><strong>Tomar tus vitaminas o tu medicación</strong> a la misma hora cada día.</li>
      </ul>

      <h2>Sueño y noches</h2>
      <ul>
        <li><strong>Estar en la cama a las 23:00.</strong></li>
        <li><strong>Nada de pantallas en la cama.</strong></li>
        <li><strong>Preparar la mochila o la ropa de mañana</strong> la noche anterior.</li>
        <li><strong>Salir a la luz de la mañana.</strong></li>
        <li><strong>Escribir tres líneas</strong> sobre tu día.</li>
      </ul>

      <h2>Mente y aprendizaje</h2>
      <ul>
        <li><strong>Leer 20 páginas.</strong> <a href="https://reliure.me/">Reliure</a>, de los mismos creadores, lleva el registro de tus libros.</li>
        <li><strong>Meditar 10 minutos.</strong> Salud cuenta tus minutos de atención plena.</li>
        <li><strong>Practicar un idioma</strong> 15 minutos.</li>
        <li><strong>Tocar un instrumento.</strong></li>
        <li><strong>Anotar algo que agradeces.</strong></li>
        <li><strong>Llamar o escribir a alguien</strong> que te importa.</li>
        <li><strong>Hacer la cama.</strong></li>
        <li><strong>Ordenar 10 minutos.</strong></li>
      </ul>

      <h2>Malos hábitos por dejar</h2>
      <p>En Coutume, un hábito por dejar se da por cumplido: solo registras el día que recaes, y cuenta tus <a href="../contador-dias-sin/">días sin</a>, el dinero ahorrado y los impulsos que resististe.</p>
      <ul>
        <li><strong><a href="../dejar-bebidas-energeticas/">Sin bebidas energéticas.</a></strong></li>
        <li><strong><a href="../dejar-de-vapear/">Sin vapear</a></strong>, o sin fumar.</li>
        <li><strong>Sin bebidas azucaradas.</strong></li>
        <li><strong>Sin picar después de cenar.</strong></li>
        <li><strong>Sin café después del mediodía.</strong></li>
        <li><strong>Sin redes sociales antes de las 9:00.</strong></li>
        <li><strong>Sin teléfono en la mesa.</strong></li>
        <li><strong>Sin pasar horas deslizando en la cama.</strong></li>
        <li><strong>Sin comida para llevar entre semana.</strong></li>
        <li><strong>Sin compras impulsivas en línea.</strong></li>
        <li><strong>Sin morderte las uñas.</strong></li>
        <li><strong>Sin posponer la alarma.</strong></li>
      </ul>

      <h2>Dinero</h2>
      <ul>
        <li><strong>Anotar cada gasto.</strong></li>
        <li><strong>Llevar tu almuerzo.</strong></li>
        <li><strong>Prepararte tu propio café.</strong> Como hábito por dejar, “sin café de cafetería” muestra el dinero que ahorras.</li>
        <li><strong>Esperar 24 horas</strong> antes de cualquier compra de más de 50 $.</li>
        <li><strong>Apartar 5 $ al día.</strong></li>
        <li><strong>Revisar tus cuentas</strong> una vez por semana.</li>
        <li><strong>Cancelar una suscripción</strong> que no usas.</li>
      </ul>

      <h2>Cómo mantenerlos</h2>
      <ul>
        <li><strong>Empieza más pequeño de lo que crees.</strong> Cinco minutos cumplidos cada día hacen más que una hora cumplida dos veces.</li>
        <li><strong>Átalo a algo que ya haces</strong>: un vaso de agua con tu café, un estiramiento después de lavarte los dientes.</li>
        <li><strong>No persigas la racha perfecta.</strong> Perder un día apenas importa; lo que importa es volver al siguiente. Por eso Coutume perdona un día perdido por semana. Lee <a href="../cuanto-tarda-un-habito/">cuánto se tarda en formar un hábito</a>.</li>
      </ul>
"""),

"howlong": dict(
  slug="cuanto-tarda-un-habito",
  title="¿Cuánto se tarda en formar un hábito? No son 21 días — Coutume",
  desc="Formar un hábito lleva 66 días de media, no 21, y entre 18 y 254 días. Lo que dice la investigación, y por qué perder un día no arruina tu progreso.",
  crumb="Cuánto tarda un hábito", guide="Lo que dice la investigación sobre el mito de los 21 días, y por qué un día perdido no importa",
  h1="¿Cuánto se tarda en formar un hábito?",
  lede="Unos 66 días de media, no 21. Y varía mucho: de 18 días a más de 250, según la persona y el hábito. La buena noticia: perder un día no te devuelve a cero.",
  body="""
      <h2>De dónde salen los 21 días</h2>
      <p>La cifra de “21 días” se remonta a los años sesenta, a un cirujano plástico, Maxwell Maltz, que observó que sus pacientes tardaban como mínimo unos 21 días en acostumbrarse a un cambio. Era una observación, no una medición de hábitos, y con los años “un mínimo de 21 días” se convirtió en “21 días”.</p>

      <h2>Lo que encontró la investigación</h2>
      <p>En un estudio publicado en línea en 2009 (en papel en 2010), un equipo del University College London dirigido por Phillippa Lally siguió a 96 personas durante 84 días. Cada una eligió una nueva conducta diaria, como beber un vaso de agua con el almuerzo o salir a correr antes de cenar, e indicó cada día hasta qué punto le resultaba automática.</p>
      <ul>
        <li>De media, la conducta tardó <strong>66 días</strong> en volverse tan automática como iba a llegar a ser.</li>
        <li>El rango fue amplio: de <strong>18 días</strong> a unos <strong>254 días</strong> estimados.</li>
        <li>Los hábitos sencillos, como beber agua, se volvieron automáticos antes que los exigentes, como hacer ejercicio.</li>
        <li><strong>Perder una ocasión no afectó de forma significativa al proceso.</strong> Lo que impedía que un hábito se formara era la falta de constancia, no perder un día.</li>
      </ul>
      <p class="note">Fuente: Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W. y Wardle, J. (2010). How are habits formed: Modelling habit formation in the real world. <em>European Journal of Social Psychology</em>, 40(6), 998–1009.</p>

      <h2>Qué significa para ti</h2>
      <ul>
        <li><strong>Cuenta con dos meses, no con tres semanas.</strong> Si un hábito todavía te cuesta después de 21 días, no te pasa nada raro.</li>
        <li><strong>Hazlo fácil.</strong> Cuanto más sencilla es la conducta, antes se vuelve automática: empieza con un vaso de agua o 5 minutos, y luego ve aumentando.</li>
        <li><strong>Mismo momento, misma señal.</strong> Repetir una conducta en la misma situación, después del café o antes de dormir, es lo que la vuelve automática.</li>
        <li><strong>Perdona el día perdido, y vuelve.</strong> Un fallo apenas importa; una pausa larga, sí.</li>
      </ul>

      <h2>Cómo sigue Coutume la investigación</h2>
      <p>Las rachas de Coutume perdonan un día perdido por semana, así que un mal día no borra semanas de esfuerzo. Tu nivel cuenta cada día que cumpliste, no solo tu racha actual, y los quince niveles van mucho más allá de 66 días, de Buena intención a Leyenda.</p>
"""),
}

if __name__ == "__main__":
    assert len(ES) == 12
