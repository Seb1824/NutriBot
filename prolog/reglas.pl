% Base de conocimiento mejorada de NutriBot

% recomendacion(Objetivo, Actividad, Dieta, Recomendacion).


% --- Perder grasa ---
recomendacion(perder_grasa, sedentario, omnivoro,
    'Deficit calorico moderado, alta ingesta de proteinas magras (pollo, pescado), muchas verduras fibrosas, reducir azucares simples y grasas saturadas. Se recomienda monitorear progreso semanal, llevar un registro de macros y ajustar calorias segun resultados.').

recomendacion(perder_grasa, moderado, omnivoro,
    'Deficit calorico controlado, proteinas magras, carbohidratos complejos integrales, ejercicio cardiovascular 3-4 veces por semana. Se recomienda pesar semanalmente, ajustar deficit segun perdida de grasa y mantener hidratacion adecuada.').

recomendacion(perder_grasa, activo, omnivoro,
    'Deficit calorico ligero, proteinas altas, carbohidratos complejos para energia, incluir entrenamiento de fuerza y cardio. Se sugiere variar rutinas, incluir dias de recuperacion activa y registrar progresion de rendimiento.').

recomendacion(perder_grasa, sedentario, vegetariano,
    'Alta proteina vegetal (legumbres, tofu), reducir carbohidratos simples, muchas verduras y frutos secos para grasas saludables. Llevar diario alimenticio, ajustar porcion de legumbres y medir evolucion semanal.').

recomendacion(perder_grasa, moderado, vegetariano,
    'Deficit calorico controlado, proteinas vegetales combinadas (legumbres, queso, tofu), carbohidratos complejos integrales y cardio moderado 3-4 veces por semana. Registrar entrenamientos, ajustar macros y asegurar aporte de micronutrientes.').

recomendacion(perder_grasa, activo, vegetariano,
    'Alto consumo de proteinas vegetales, carbohidratos complejos (quinoa, arroz integral), grasas saludables y entrenamiento regular. Se recomienda periodizacion de intensidad, seguimiento de energia y adaptacion de dieta segun progreso.').

recomendacion(perder_grasa, sedentario, vegano,
    'Deficit calorico con enfasis en legumbres, tofu, tempeh, verduras variadas, controlar grasas y evitar azucares refinados. Llevar registro de ingesta de B12 y Omega3, ajustar volumen de entrenamiento ligero y registrar peso.').

recomendacion(perder_grasa, moderado, vegano,
    'Deficit calorico controlado con enfasis en legumbres, tofu y tempeh, carbohidratos integrales (quinoa, avena), verduras variadas y cardio moderado regular. Se sugiere suplementar B12, llevar control de macros y variar fuentes de proteina vegetal.').

recomendacion(perder_grasa, activo, vegano,
    'Proteinas vegetales altas, carbohidratos complejos integrales, grasas saludables como aguacate y nueces, actividad fisica constante. Monitorear recuperacion, ajustar macros semanalmente y planificar dias de descanso activo.').

% --- Subir masa muscular ---
recomendacion(subir_masa, sedentario, omnivoro,
    'Superavit calorico con enfasis en proteinas magras (carne, huevo, lacteos), carbohidratos complejos, evitar grasas saturadas y aumentar actividad fisica progresivamente. Se recomienda registrar fuerza, ajustar superavit y periodizar volumen de entrenamiento.').

recomendacion(subir_masa, moderado, omnivoro,
    'Superavit calorico moderado, alta proteina, carbohidratos complejos, entrenamiento de fuerza 3-5 veces por semana. Llevar diario de cargas, ajustar calorias semanalmente y asegurar recuperacion muscular.').

recomendacion(subir_masa, activo, omnivoro,
    'Alto superavit calorico, proteina alta para reparacion muscular, carbohidratos para energia, grasas saludables y entrenamiento intenso de fuerza. Se recomienda ciclos de intensidad, seguimiento de progreso y ajuste de macros cada dos semanas.').

recomendacion(subir_masa, sedentario, vegetariano,
    'Incrementar calorias con proteinas vegetales (legumbres, queso, huevos), carbohidratos integrales, grasas saludables y comenzar actividad fisica ligera. Registrar progresion inicial, ajustar superavit y asegurar aporte de hierro y B12.').

recomendacion(subir_masa, moderado, vegetariano,
    'Superavit calorico moderado, proteinas vegetales y lacteos (legumbres, huevos, queso), carbohidratos complejos y entrenamiento de fuerza 4 veces por semana. Llevar registro de cargas, variar fuentes de proteina y controlar resultados.').

recomendacion(subir_masa, activo, vegetariano,
    'Superavit calorico alto, proteinas vegetales combinadas, carbohidratos complejos, grasas saludables y rutina regular de fuerza. Se sugiere periodizacion progresiva, registro de rendimiento y ajuste de macros segun ganancias.').

recomendacion(subir_masa, sedentario, vegano,
    'Superavit calorico con legumbres, tofu, tempeh, frutos secos, carbohidratos integrales, y aumentar actividad fisica gradual. Registrar energia diaria, asegurar suplemente de B12 y Omega3, y ajustar superavit.').

recomendacion(subir_masa, moderado, vegano,
    'Superavit calorico moderado con proteinas vegetales completas (tofu, tempeh, legumbres + cereales), carbohidratos integrales, grasas saludables y rutina de fuerza regular. Llevar dato de progresion, ajustar macros y asegurar recuperacion.').

recomendacion(subir_masa, activo, vegano,
    'Alto superavit calorico con proteinas vegetales completas, carbohidratos integrales, grasas saludables, entrenamiento de fuerza intenso. Se recomienda seguimiento de volumen muscular, ajuste de macros y descanso estrategico.').

% --- Mantener peso ---
recomendacion(mantener_peso, sedentario, omnivoro,
    'Consumo calorico estable, balance de macronutrientes, actividad fisica ligera y evitar alimentos ultraprocesados. Se recomienda medir peso mensualmente, ajustar macros y mantener hidratacion.').

recomendacion(mantener_peso, moderado, omnivoro,
    'Dieta equilibrada con proteinas magras, carbohidratos integrales, grasas saludables y actividad fisica regular. Llevar registro de energia, ajustar dias de descanso y variar fuentes de nutrientes.').

recomendacion(mantener_peso, activo, omnivoro,
    'Dieta balanceada que soporte gasto energetico, proteinas adecuadas, carbohidratos para energia, grasas saludables. Se recomienda seguimiento de rendimiento, ajuste de porcions y planificacion de comidas.').

recomendacion(mantener_peso, sedentario, vegetariano,
    'Consumo calorico adecuado con proteinas vegetales, grasas saludables y control de carbohidratos refinados. Llevar diario de alimentos, ajustar macros y asegurar aporte de micronutrientes.').

recomendacion(mantener_peso, moderado, vegetariano,
    'Dieta variada rica en legumbres, cereales integrales, vegetales y grasas saludables, con actividad fisica moderada. Registrar energia gastada, ajustar menus y variar fuentes proteicas.').

recomendacion(mantener_peso, activo, vegetariano,
    'Mantener balance energetico, alta variedad de proteinas vegetales, carbohidratos complejos y grasas saludables, actividad fisica constante. Se recomienda seguimiento de rendimiento y ajuste mensual de macros.').

recomendacion(mantener_peso, sedentario, vegano,
    'Dieta balanceada con legumbres, cereales, verduras, grasas saludables, evitando excesos de azucares y grasas trans. Llevar registro de ingesta, ajustar volumen de comida y asegurar suplementos de B12.').

recomendacion(mantener_peso, moderado, vegano,
    'Consumo calorico estable con variedad de alimentos vegetales, proteinas vegetales combinadas y actividad fisica regular. Registrar energia gastada, ajustar macros y variar fuentes de nutrientes.').

recomendacion(mantener_peso, activo, vegano,
    'Dieta equilibrada con proteinas vegetales completas, carbohidratos integrales y grasas saludables, con actividad fisica constante. Se sugiere medir rendimiento, ajustar comidas y asegurar hidratacion continua.').

recomendacion(mejorar_salud_digestiva, sedentario, omnivoro,'Reducir consumo de grasas trans y procesados, aumentar fibra y mantenerse hidratado. Incluir caminatas ligeras tras comidas.').
recomendacion(mejorar_salud_digestiva, sedentario, vegetariano, 'Consumir avena, lentejas, frutas suaves; evitar frituras. Agregar alimentos fermentados y caminar diariamente.').
recomendacion(mejorar_salud_digestiva, sedentario, vegano, 'Dieta rica en frutas cocidas, vegetales sin piel y cereales integrales suaves. Evitar irritantes intestinales.').
recomendacion(mejorar_salud_digestiva, sedentario, ayuno_variable, 'Incluir alimentos bajos en FODMAPs durante ventana de alimentacion. Ayunos maximo de 12 horas para no irritar intestino.').

recomendacion(mejorar_salud_digestiva, moderado, omnivoro, 'Incluir pescado azul, arroz integral y yogur. Evitar picantes y ajustar dieta segun sintomas digestivos.').
recomendacion(mejorar_salud_digestiva, moderado, vegetariano, 'Dieta variada rica en fibra soluble, legumbres suaves y probioticos. Registrar respuesta digestiva diaria.').
recomendacion(mejorar_salud_digestiva, moderado, vegano, 'Evitar alimentos fermentables, incluir linaza y chia, priorizar frutas cocidas. Actividad moderada tras cada comida.').
recomendacion(mejorar_salud_digestiva, moderado, ayuno_variable, 'Ventana alimentaria de 10 horas, evitar comidas grandes nocturnas y llevar diario de sintomas.').

recomendacion(mejorar_salud_digestiva, activo, omnivoro, 'Alta ingesta de fibra insoluble de frutas y verduras, suplementar probioticos si necesario. Cuidar volumen de comidas.').
recomendacion(mejorar_salud_digestiva, activo, vegetariano, 'Evitar exceso de legumbres sin coccion adecuada, incluir frutas suaves y mantener ritmo digestivo estable.').
recomendacion(mejorar_salud_digestiva, activo, vegano, 'Frutas cocidas, cereales suaves y evitar alimentos irritantes. Ejercicio postprandial moderado.').
recomendacion(mejorar_salud_digestiva, activo, ayuno_variable, 'Ayuno controlado (14h), dieta rica en verduras cocidas y grasas saludables. Evitar cafe y picantes.').

recomendacion(perder_grasa, intermitente, omnivoro, 'Ayuno 16:8 combinado con deficit calorico, proteinas altas y entrenamiento ligero en ayunas. Controlar energia y evitar atracones post-ayuno.').
recomendacion(perder_grasa, intermitente, vegetariano, 'Ayuno intermitente 14:10 con proteinas vegetales, grasas saludables y monitoreo de energia. Ajustar ventana si hay fatiga.').
recomendacion(perder_grasa, intermitente, vegano, 'Planificar ingestas balanceadas durante ventana de 10 horas, enfocar en fibra y evitar azucares. Registrar hambre y saciedad.').
recomendacion(perder_grasa, intermitente, ayuno_variable, 'Alternar dias de ayuno 14-16h con alimentos vegetales ricos en fibra y bajos en calorias.').

recomendacion(subir_masa, intermitente, omnivoro, 'Planificar dos comidas densas en ventana de 8h, altas en proteina animal y carbohidratos complejos. Priorizar recuperacion post-entrenamiento.').
recomendacion(subir_masa, intermitente, vegetariano, 'Incluir legumbres, huevos y cereales completos. Entrenamiento en la tarde y cena proteica antes del cierre de ventana.').
recomendacion(subir_masa, intermitente, vegano, 'Altas calorias en poco tiempo: aguacate, tofu, arroz. Ayuno no mayor a 14h para mantener anabolismo.').
recomendacion(subir_masa, intermitente, ayuno_variable, 'Ayunos variables con enfasis en dias de superavit, usando batidos densos en nutrientes en ventana de comida.').

recomendacion(mantener_peso, intermitente, omnivoro, 'Mantener balance calórico durante 10h de ventana. Comer despacio, controlar porciones y evitar snacks nocturnos.').
recomendacion(mantener_peso, intermitente, vegetariano, 'Ventana 12:12, comida rica en vegetales, huevos y cereales. Ajustar si se presentan bajones de energia.').
recomendacion(mantener_peso, intermitente, vegano, 'Planificar comidas completas y evitar exceso de fruta en ayuno. Priorizar vegetales cocidos y grasas saludables.').
recomendacion(mantener_peso, intermitente, ayuno_variable, 'Adaptar ayuno segun nivel de hambre. Priorizar densidad nutricional y mantener ingesta equilibrada.').

recomendacion(perder_grasa, sedentario, ayuno_variable,
    'Implementar ayuno 12:12 para comenzar, enfocando las comidas en vegetales, legumbres y proteinas ligeras. Monitorear energia y ajustar ventana gradualmente.').

recomendacion(perder_grasa, moderado, ayuno_variable,
    'Practicar ayunos de 14h con comidas controladas en calorias, priorizando fibra, grasas saludables y proteinas. Ejercicio ligero durante la mañana.').

recomendacion(perder_grasa, activo, ayuno_variable,
    'Ayuno flexible (14-16h) acompañado de alimentacion densa en nutrientes. Entrenamientos en ayunas seguidos de comidas con proteinas y vegetales.').

recomendacion(subir_masa, sedentario, ayuno_variable,
    'Ayuno 10:14 con comidas calóricas ricas en proteina y grasas saludables. Incluir batidos densos y aumentar actividad ligera progresivamente.').

recomendacion(subir_masa, moderado, ayuno_variable,
    'Ayuno 8:16 en dias de entrenamiento con enfasis en comidas post-entreno densas en carbohidratos y proteinas. Asegurar descanso adecuado.').

recomendacion(subir_masa, activo, ayuno_variable,
    'Alternar dias de ayuno 8-10h con comidas grandes y completas. Uso de batidos de alta energia para cubrir necesidades caloricas sin saturar.').

recomendacion(mantener_peso, sedentario, ayuno_variable,
    'Ayuno 12:12 con enfoque en comidas balanceadas y ligeras. Evitar azucares procesados, mantener caminatas diarias y buena hidratacion.').

recomendacion(mantener_peso, moderado, ayuno_variable,
    'Ventana alimentaria de 10 horas con dieta equilibrada en macros. Actividad moderada diaria y ajuste segun niveles de energia y saciedad.').

recomendacion(mantener_peso, activo, ayuno_variable,
    'Ayuno flexible con comidas densas en nutrientes, proteinas completas y carbohidratos integrales. Ajustar segun requerimiento energetico diario.').

% Regla general para dar la recomendación
nutricion(Objetivo, Actividad, Dieta, Recomendacion) :-
    recomendacion(Objetivo, Actividad, Dieta, Recomendacion).
