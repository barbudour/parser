# CardTypeExtensionType.Registry - свойство
Реестр, содержащий все зарегистрированные типы.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override IRegistry<Guid, CardTypeExtensionType> Registry { get; }
VB __Копировать
     Protected Overrides ReadOnly Property Registry As IRegistry(Of Guid, CardTypeExtensionType)
    	Get
C++ __Копировать
     protected:
    virtual property IRegistry<Guid, CardTypeExtensionType^>^ Registry {
    	IRegistry<Guid, CardTypeExtensionType^>^ get () override;
    }
F# __Копировать
     abstract Registry : IRegistry<Guid, CardTypeExtensionType> with get
    override Registry : IRegistry<Guid, CardTypeExtensionType> with get
#### Значение свойства
[IRegistry](T_Tessa_Platform_IRegistry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CardTypeExtensionType](T_Tessa_Cards_CardTypeExtensionType.htm)>
##  __См. также
#### Ссылки
[CardTypeExtensionType - ](T_Tessa_Cards_CardTypeExtensionType.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
