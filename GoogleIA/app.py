from flask import Flask, render_template

app = Flask(__name__)

# Aquí es donde almacenarías el contenido de tus resúmenes
# Reemplaza el contenido de 'resumen_ampliado' con el de tus artículos
resumen_ampliado = {
    "introductorio": """
    <p>¡Bienvenidos a un espacio donde exploraremos cómo la tecnología está transformando la educación y la sociedad! En la era digital en la que vivimos, es crucial entender cómo las herramientas tecnológicas, como la inteligencia artificial, los videojuegos y las plataformas en línea, pueden mejorar la forma en que aprendemos y nos relacionamos. No solo hablaremos de computadoras, sino de cómo estas herramientas pueden ayudarnos a ser más creativos, a resolver problemas y a aprender de maneras nuevas y emocionantes.</p>
    <p>Este resumen integrador se basa en el análisis de cinco artículos científicos que abordan temas clave como la inteligencia artificial en la educación superior, el uso de videojuegos para el aprendizaje, la brecha digital y la importancia de la educación inclusiva en el entorno digital. Nuestro objetivo es que, sin importar tu nivel de conocimiento previo, puedas comprender la importancia de estos temas y cómo nos afectan a todos.</p>
    <p>Prepárate para descubrir cómo la tecnología puede ser una poderosa aliada para construir un futuro educativo y social más justo y equitativo. ¡Empecemos!</p>
    """,
    "tecnico": """
    <h3>Inteligencia Artificial en la Educación Superior</h3>
    <p>La integración de la Inteligencia Artificial (IA) en la educación superior presenta un paradigma disruptivo, redefiniendo las metodologías pedagógicas y los procesos de aprendizaje. Los artículos analizados enfatizan el potencial de la IA para personalizar rutas de aprendizaje adaptativas, proporcionar retroalimentación automatizada y optimizar la gestión de recursos educativos. Se exploran sistemas basados en IA para la tutorización inteligente, la evaluación formativa y la identificación de patrones de rendimiento académico. Sin embargo, se subraya la necesidad de abordar desafíos éticos, la transparencia algorítmica y la capacitación docente para una implementación efectiva.</p>

    <h3>Videojuegos y Aprendizaje</h3>
    <p>El uso de videojuegos en entornos educativos, conceptualizado como "aprendizaje basado en juegos" o "gamificación", emerge como una estrategia pedagógica innovadora. Se argumenta que los videojuegos, por su inherente capacidad de engagement, retroalimentación inmediata y estructuras de recompensa, pueden potenciar el desarrollo de habilidades cognitivas complejas como el pensamiento crítico, la resolución de problemas y la colaboración. Se analizan estudios que demuestran la efectividad de los videojuegos para el aprendizaje de conceptos abstractos, el desarrollo de la creatividad y la motivación intrínseca. Se resalta la importancia de un diseño pedagógico cuidadoso para integrar los juegos de manera significativa en el currículo.</p>

    <h3>Brecha Digital y Educación Inclusiva</h3>
    <p>La brecha digital, entendida como la disparidad en el acceso y uso de las Tecnologías de la Información y Comunicación (TIC), persiste como un obstáculo significativo para la equidad educativa. Los artículos abordan las dimensiones de la brecha digital (acceso, uso y habilidades) y sus implicaciones para grupos vulnerables. Se proponen estrategias para fomentar la inclusión digital, incluyendo políticas públicas de acceso a infraestructura, programas de alfabetización digital y el desarrollo de recursos educativos abiertos (REA) accesibles. Se enfatiza la necesidad de un enfoque holístico que considere factores socioeconómicos y culturales para mitigar estas desigualdades.</p>

    <h3>Aprendizaje Ubicuo y Conectivismo</h3>
    <p>El aprendizaje ubicuo (u-learning), facilitado por dispositivos móviles y redes inalámbricas, redefine el espacio y tiempo del aprendizaje, permitiendo que ocurra en cualquier momento y lugar. Este concepto se vincula estrechamente con la teoría del conectivismo, que postula que el aprendizaje se produce a través de la formación de conexiones en redes de información y conocimiento. Los artículos exploran cómo la ubicuidad tecnológica promueve la autonomía del estudiante, el aprendizaje informal y la construcción colaborativa del conocimiento. Se analizan plataformas y herramientas que facilitan el u-learning, así como los desafíos en su implementación, como la sobrecarga de información y la necesidad de desarrollar habilidades de curación de contenido.</p>

    <h3>Desarrollo de Competencias Digitales Docentes</h3>
    <p>La transformación digital en la educación requiere que los docentes desarrollen un conjunto robusto de competencias digitales. Los artículos analizan marcos de competencias digitales docentes que incluyen dimensiones pedagógicas, tecnológicas y éticas. Se enfatiza la necesidad de programas de formación docente que aborden el diseño de experiencias de aprendizaje mediadas por tecnología, el uso crítico de herramientas digitales, la gestión de la información y la promoción de la ciudadanía digital en los estudiantes. Se discute la importancia de la actualización continua y el desarrollo profesional para que los educadores puedan aprovechar plenamente el potencial de las TIC en sus prácticas.</p>
    """,
    "reflexivo": """
    <p>La convergencia de las tecnologías digitales y la educación nos invita a una profunda reflexión sobre el futuro del aprendizaje y la construcción social del conocimiento. Más allá de la implementación de herramientas, ¿estamos realmente formando ciudadanos críticos, creativos y éticos para la sociedad del siglo XXI? La inteligencia artificial, si bien promete personalizar el aprendizaje, ¿corre el riesgo de homogeneizarlo o de perpetuar sesgos algorítmicos si no se diseña con una perspectiva inclusiva?</p>
    <p>El entusiasmo por la gamificación debe equilibrarse con una mirada crítica: ¿estamos fomentando una motivación intrínseca por el conocimiento o simplemente condicionando el aprendizaje a sistemas de recompensa extrínsecos? La brecha digital, lejos de ser solo un problema de acceso a dispositivos, ¿no es también una brecha de competencias y de pensamiento crítico frente a la infodemia y la desinformación? ¿Cómo aseguramos que el aprendizaje ubicuo no se convierta en una sobrecarga cognitiva, y cómo cultivamos la capacidad de discernimiento en un mar de información?</p>
    <p>La formación docente en competencias digitales es crucial, pero ¿estamos capacitando a los educadores para ser facilitadores de experiencias auténticas o meros operadores de plataformas? La verdadera transformación educativa no reside solo en la adopción tecnológica, sino en la redefinición de los roles, las metodologías y, fundamentalmente, en la promoción de un aprendizaje significativo que empodere a los individuos para comprender, transformar y participar activamente en un mundo cada vez más complejo y digitalizado.</p>
    <p>Este análisis nos impulsa a ir más allá de la superficie de las soluciones tecnológicas para cuestionar sus implicaciones profundas, sus oportunidades y sus riesgos, siempre con el objetivo de construir una educación más equitativa, relevante y humana en la era digital.</p>
    """
}

@app.route('/')
def index():
    return render_template('index.html', resumen=resumen_ampliado)

if __name__ == '__main__':
    app.run(debug=True)