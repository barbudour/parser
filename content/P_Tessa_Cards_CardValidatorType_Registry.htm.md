# CardValidatorType.Registry - свойство
Реестр, содержащий все зарегистрированные типы.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override IRegistry<Guid, CardValidatorType> Registry { get; }
VB __Копировать
     Protected Overrides ReadOnly Property Registry As IRegistry(Of Guid, CardValidatorType)
    	Get
C++ __Копировать
     protected:
    virtual property IRegistry<Guid, CardValidatorType^>^ Registry {
    	IRegistry<Guid, CardValidatorType^>^ get () override;
    }
F# __Копировать
     abstract Registry : IRegistry<Guid, CardValidatorType> with get
    override Registry : IRegistry<Guid, CardValidatorType> with get
#### Значение свойства
[IRegistry](T_Tessa_Platform_IRegistry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CardValidatorType](T_Tessa_Cards_CardValidatorType.htm)>
##  __См. также
#### Ссылки
[CardValidatorType - ](T_Tessa_Cards_CardValidatorType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
