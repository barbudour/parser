# Tessa.Cards.Validation - пространство имён
API серверной валидации карточек.
##  __Классы
[CardValidationContext](T_Tessa_Cards_Validation_CardValidationContext.htm)|
Контекст валидации карточки, содержащий проверяемые данные карточки и методы
получения объектов, которые выполняют построение результата валидации для
различных элементов проверяемой карточки.  
---|---  
[CardValidationExtensions](T_Tessa_Cards_Validation_CardValidationExtensions.htm)|
Методы-расширения для пространства имён Tessa.Cards.Validation.  
[CardValidationLimitationManager](T_Tessa_Cards_Validation_CardValidationLimitationManager.htm)|
Объект, ограничивающий доступность объектов для валидации.  
[CardValidationManager](T_Tessa_Cards_Validation_CardValidationManager.htm)|
Объект, управляющий валидацией карточки.  
[CardValidationNotNullTableInfo](T_Tessa_Cards_Validation_CardValidationNotNullTableInfo.htm)|
Информация по секции, для которой требуется выполнить валидацию для валидатора
[NotNullTable](F_Tessa_Cards_CardValidatorTypes_NotNullTable.htm).  
[CardValidationResult](T_Tessa_Cards_Validation_CardValidationResult.htm)|
Представляет отсутствующий результат валидации.  
[CardValidationUniqueInfo](T_Tessa_Cards_Validation_CardValidationUniqueInfo.htm)|
Информация по секции и колонке, для которой требуется выполнить валидацию для
валидатора [Unique](F_Tessa_Cards_CardValidatorTypes_Unique.htm).  
[CardValidatorHelper](T_Tessa_Cards_Validation_CardValidatorHelper.htm)|
Вспомогательные методы для валидаторов.  
[CardValidatorRegistry](T_Tessa_Cards_Validation_CardValidatorRegistry.htm)|
Реестр экземпляров валидаторов карточки. Допустимо создавать несколько
экземпляров реестров, содержащих различные наборы экземпляров валидаторов.  
[CardValidatorSettings](T_Tessa_Cards_Validation_CardValidatorSettings.htm)|
Настройки стандартных валидаторов.  
[UniqueValidatorHelper](T_Tessa_Cards_Validation_UniqueValidatorHelper.htm)|
Вспомогательные методы для проверки уникальности.  
## __Интерфейсы
[ICardValidationContext](T_Tessa_Cards_Validation_ICardValidationContext.htm)|
Контекст валидации карточки, содержащий проверяемые данные карточки и методы
получения объектов, которые выполняют построение результата валидации для
различных элементов проверяемой карточки.  
---|---  
[ICardValidationLimitationManager](T_Tessa_Cards_Validation_ICardValidationLimitationManager.htm)|
Объект, ограничивающий доступность объектов для валидации.  
[ICardValidationManager](T_Tessa_Cards_Validation_ICardValidationManager.htm)|
Объект, управляющий валидацией карточки.  
[ICardValidationResult](T_Tessa_Cards_Validation_ICardValidationResult.htm)|
Результат валидации карточки, содержащий методы доступа к построенным
результату валидации для различных элементов проверяемой карточки.  
[ICardValidator](T_Tessa_Cards_Validation_ICardValidator.htm)|  Валидатор
карточки. Экземпляры валидаторов не должны иметь состояния, т.е. полей,
изменяемых со временем. Конструктор валидатора будет вызван в момент
регистрации экземпляра в реестре
[ICardValidatorRegistry](T_Tessa_Cards_Validation_ICardValidatorRegistry.htm).  
[ICardValidatorRegistry](T_Tessa_Cards_Validation_ICardValidatorRegistry.htm)|
Реестр валидаторов карточки.  
## __Перечисления
[CardValidationMode](T_Tessa_Cards_Validation_CardValidationMode.htm)|  Способ
выполнения валидации.  
---|---
