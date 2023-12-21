# NumberType.Registry - свойство
Реестр, содержащий все зарегистрированные типы.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override IRegistry<Guid, NumberType> Registry { get; }
VB __Копировать
     Protected Overrides ReadOnly Property Registry As IRegistry(Of Guid, NumberType)
    	Get
C++ __Копировать
     protected:
    virtual property IRegistry<Guid, NumberType^>^ Registry {
    	IRegistry<Guid, NumberType^>^ get () override;
    }
F# __Копировать
     abstract Registry : IRegistry<Guid, NumberType> with get
    override Registry : IRegistry<Guid, NumberType> with get
#### Значение свойства
[IRegistry](T_Tessa_Platform_IRegistry_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[NumberType](T_Tessa_Cards_Numbers_NumberType.htm)>
##  __См. также
#### Ссылки
[NumberType - ](T_Tessa_Cards_Numbers_NumberType.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
