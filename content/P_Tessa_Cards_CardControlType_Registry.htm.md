# CardControlType.Registry - свойство
Реестр, содержащий все зарегистрированные типы.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override IRegistry<Guid, CardControlType> Registry { get; }
VB __Копировать
     Protected Overrides ReadOnly Property Registry As IRegistry(Of Guid, CardControlType)
    	Get
C++ __Копировать
     protected:
    virtual property IRegistry<Guid, CardControlType^>^ Registry {
    	IRegistry<Guid, CardControlType^>^ get () override;
    }
F# __Копировать
     abstract Registry : IRegistry<Guid, CardControlType> with get
    override Registry : IRegistry<Guid, CardControlType> with get
#### Значение свойства
[IRegistry](T_Tessa_Platform_IRegistry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CardControlType](T_Tessa_Cards_CardControlType.htm)>
##  __См. также
#### Ссылки
[CardControlType - ](T_Tessa_Cards_CardControlType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
