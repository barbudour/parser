# CardValidatorRegistry.GetAll - метод
Возвращает коллекцию экземпляров валидаторов, типы которых были
зарегистрированы в реестре.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICollection<ICardValidator> GetAll()
VB __Копировать
     Public Function GetAll As ICollection(Of ICardValidator)
C++ __Копировать
     public:
    virtual ICollection<ICardValidator^>^ GetAll() sealed
F# __Копировать
     abstract GetAll : unit -> ICollection<ICardValidator> 
    override GetAll : unit -> ICollection<ICardValidator> 
#### Возвращаемое значение
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[ICardValidator](T_Tessa_Cards_Validation_ICardValidator.htm)>  
Коллекция экземпляров валидаторов, типы которых были зарегистрированы в
реестре.
#### Реализации
[ICardValidatorRegistry.GetAll()](M_Tessa_Cards_Validation_ICardValidatorRegistry_GetAll.htm)  
##  __См. также
#### Ссылки
[CardValidatorRegistry - ](T_Tessa_Cards_Validation_CardValidatorRegistry.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
