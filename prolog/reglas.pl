% Base de conocimiento mejorada de NutriBot

% recomendacion(Objetivo, Actividad, Dieta, Recomendacion).

% --- Perder grasa ---

recomendacion(perder_grasa, sedentario, omnivoro,
    'Déficit calórico moderado, alta ingesta de proteínas magras (pollo, pescado), muchas verduras fibrosas, reducir azúcares simples y grasas saturadas.').

recomendacion(perder_grasa, moderado, omnivoro,
    'Déficit calórico controlado, proteínas magras, carbohidratos complejos integrales, ejercicio cardiovascular 3-4 veces por semana.').

recomendacion(perder_grasa, activo, omnivoro,
    'Déficit calórico ligero, proteínas altas, carbohidratos complejos para energía, incluir entrenamiento de fuerza y cardio.').

recomendacion(perder_grasa, sedentario, vegetariano,
    'Alta proteína vegetal (legumbres, tofu), reducir carbohidratos simples, muchas verduras y frutos secos para grasas saludables.').

recomendacion(perder_grasa, activo, vegetariano,
    'Alto consumo de proteínas vegetales, carbohidratos complejos (quinoa, arroz integral), grasas saludables y entrenamiento regular.').

recomendacion(perder_grasa, sedentario, vegano,
    'Déficit calórico con énfasis en legumbres, tofu, tempeh, verduras variadas, controlar grasas y evitar azúcares refinados.').

recomendacion(perder_grasa, activo, vegano,
    'Proteínas vegetales altas, carbohidratos complejos integrales, grasas saludables como aguacate y nueces, actividad física constante.').

% --- Subir masa muscular ---

recomendacion(subir_masa, sedentario, omnivoro,
    'Superávit calórico con énfasis en proteínas magras (carne, huevo, lácteos), carbohidratos complejos, evitar grasas saturadas y aumentar actividad física progresivamente.').

recomendacion(subir_masa, moderado, omnivoro,
    'Superávit calórico moderado, alta proteína, carbohidratos complejos, entrenamiento de fuerza 3-5 veces por semana.').

recomendacion(subir_masa, activo, omnivoro,
    'Alto superávit calórico, proteína alta para reparación muscular, carbohidratos para energía, grasas saludables y entrenamiento intenso de fuerza.').

recomendacion(subir_masa, sedentario, vegetariano,
    'Incrementar calorías con proteínas vegetales (legumbres, queso, huevos), carbohidratos integrales, grasas saludables y comenzar actividad física ligera.').

recomendacion(subir_masa, activo, vegetariano,
    'Superávit calórico alto, proteínas vegetales combinadas, carbohidratos complejos, grasas saludables y rutina regular de fuerza.').

recomendacion(subir_masa, sedentario, vegano,
    'Superávit calórico con legumbres, tofu, tempeh, frutos secos, carbohidratos integrales, y aumentar actividad física gradual.').

recomendacion(subir_masa, activo, vegano,
    'Alto superávit calórico con proteínas vegetales completas, carbohidratos integrales, grasas saludables, entrenamiento de fuerza intenso.').

% --- Mantener peso ---

recomendacion(mantener_peso, sedentario, omnivoro,
    'Consumo calórico estable, balance de macronutrientes, actividad física ligera y evitar alimentos ultraprocesados.').

recomendacion(mantener_peso, moderado, omnivoro,
    'Dieta equilibrada con proteínas magras, carbohidratos integrales, grasas saludables y actividad física regular.').

recomendacion(mantener_peso, activo, omnivoro,
    'Dieta balanceada que soporte gasto energético, proteínas adecuadas, carbohidratos para energía, grasas saludables.').

recomendacion(mantener_peso, sedentario, vegetariano,
    'Consumo calórico adecuado con proteínas vegetales, grasas saludables y control de carbohidratos refinados.').

recomendacion(mantener_peso, moderado, vegetariano,
    'Dieta variada rica en legumbres, cereales integrales, vegetales y grasas saludables, con actividad física moderada.').

recomendacion(mantener_peso, activo, vegetariano,
    'Mantener balance energético, alta variedad de proteínas vegetales, carbohidratos complejos y grasas saludables, actividad física constante.').

recomendacion(mantener_peso, sedentario, vegano,
    'Dieta balanceada con legumbres, cereales, verduras, grasas saludables, evitando excesos de azúcares y grasas trans.').

recomendacion(mantener_peso, moderado, vegano,
    'Consumo calórico estable con variedad de alimentos vegetales, proteínas vegetales combinadas y actividad física regular.').

recomendacion(mantener_peso, activo, vegano,
    'Dieta equilibrada con proteínas vegetales completas, carbohidratos integrales y grasas saludables, con actividad física constante.').

% Regla general para dar la recomendación
nutricion(Objetivo, Actividad, Dieta, Recomendacion) :-
    recomendacion(Objetivo, Actividad, Dieta, Recomendacion).
