# DefaultCardTypeExtensionTypes.Register - метод
Регистрирует все стандартные типы посредством заданного метода.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Cards](N_Tessa_Extensions_Default_Shared_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void Register(
    	Action<CardTypeExtensionType> registerAction
    )
VB __Копировать
     Public Shared Sub Register ( 
    	registerAction As Action(Of CardTypeExtensionType)
    )
C++ __Копировать
     public:
    static void Register(
    	Action<CardTypeExtensionType^>^ registerAction
    )
F# __Копировать
     static member Register : 
            registerAction : Action<CardTypeExtensionType> -> unit 
#### Параметры
registerAction
[Action](https://learn.microsoft.com/dotnet/api/system.action-1)<[CardTypeExtensionType](T_Tessa_Cards_CardTypeExtensionType.htm)>
    Метод, выполняющий регистрацию типа.
##  __См. также
#### Ссылки
[DefaultCardTypeExtensionTypes -
](T_Tessa_Extensions_Default_Shared_Cards_DefaultCardTypeExtensionTypes.htm)
[Tessa.Extensions.Default.Shared.Cards - пространство
имён](N_Tessa_Extensions_Default_Shared_Cards.htm)
