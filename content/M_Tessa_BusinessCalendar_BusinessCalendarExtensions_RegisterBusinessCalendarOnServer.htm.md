# BusinessCalendarExtensions.RegisterBusinessCalendarOnServer - метод
Выполняет регистрацию API бизнес-календаря на сервере.
## __Definition
 **Пространство имён:** [Tessa.BusinessCalendar](N_Tessa_BusinessCalendar.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IUnityContainer RegisterBusinessCalendarOnServer(
    	this IUnityContainer unityContainer
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterBusinessCalendarOnServer ( 
    	unityContainer As IUnityContainer
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IUnityContainer^ RegisterBusinessCalendarOnServer(
    	IUnityContainer^ unityContainer
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterBusinessCalendarOnServer : 
            unityContainer : IUnityContainer -> IUnityContainer 
#### Параметры
unityContainer IUnityContainer
    Контейнер Unity, в котором выполняется регистрация.
#### Возвращаемое значение
IUnityContainer  
Контейнер unityContainer для цепочки вызовов.
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
[BusinessCalendarExtensions -
](T_Tessa_BusinessCalendar_BusinessCalendarExtensions.htm)
[Tessa.BusinessCalendar - пространство имён](N_Tessa_BusinessCalendar.htm)
