# CardValidatorRegistry.Get - метод
Возвращает экземпляр валидатора, тип которого был зарегистрирован в реестре по
метаинформации о типе этого валидатора.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardValidator Get(
    	CardValidatorType type
    )
VB __Копировать
     Public Function Get ( 
    	type As CardValidatorType
    ) As ICardValidator
C++ __Копировать
     public:
    virtual ICardValidator^ Get(
    	CardValidatorType^ type
    ) sealed
F# __Копировать
     abstract Get : 
            type : CardValidatorType -> ICardValidator 
    override Get : 
            type : CardValidatorType -> ICardValidator 
#### Параметры
type [CardValidatorType](T_Tessa_Cards_CardValidatorType.htm)
    Метаинформация о типе валидаторе, экземпляр которого требуется получить.
#### Возвращаемое значение
[ICardValidator](T_Tessa_Cards_Validation_ICardValidator.htm)  
Экземпляр зарегистрированного типа валидатора.
#### Реализации
[ICardValidatorRegistry.Get(CardValidatorType)](M_Tessa_Cards_Validation_ICardValidatorRegistry_Get.htm)  
##  __См. также
#### Ссылки
[CardValidatorRegistry - ](T_Tessa_Cards_Validation_CardValidatorRegistry.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
