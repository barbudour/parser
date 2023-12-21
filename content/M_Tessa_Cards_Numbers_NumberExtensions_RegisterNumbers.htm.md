# NumberExtensions.RegisterNumbers - метод
Выполняет регистрацию API работы с номерами. Метод автоматически вызывается
при регистрации серверного или клиентского API по работе с карточками.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IUnityContainer RegisterNumbers(
    	this IUnityContainer container,
    	SessionType sessionType
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterNumbers ( 
    	container As IUnityContainer,
    	sessionType As SessionType
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IUnityContainer^ RegisterNumbers(
    	IUnityContainer^ container, 
    	SessionType sessionType
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterNumbers : 
            container : IUnityContainer * 
            sessionType : SessionType -> IUnityContainer 
#### Параметры
container IUnityContainer
    Контейнер Unity.
sessionType [SessionType](T_Tessa_Platform_Runtime_SessionType.htm)
    Тип сессии, определяющий, выполняется ли регистрация на клиенте или на сервере.
#### Возвращаемое значение
IUnityContainer  
Контейнер Unity container для цепочки вызовов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа IUnityContainer. При вызове метода для экземпляра следует
опускать первый параметр. Дополнительные сведения см. в разделе [Методы
расширения (Visual Basic)](https://docs.microsoft.com/dotnet/visual-
basic/programming-guide/language-features/procedures/extension-methods) или
[Методы расширения (Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[NumberExtensions - ](T_Tessa_Cards_Numbers_NumberExtensions.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
