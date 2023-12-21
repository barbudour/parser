# EDSExtensions.RegisterCryptoAPI - метод
Выполняет регистрацию криптографических API, доступных на сервере.
## __Definition
 **Пространство имён:** [Tessa.EDS](N_Tessa_EDS.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public static IUnityContainer RegisterCryptoAPI(
    	this IUnityContainer container
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterCryptoAPI ( 
    	container As IUnityContainer
    ) As IUnityContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IUnityContainer^ RegisterCryptoAPI(
    	IUnityContainer^ container
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterCryptoAPI : 
            container : IUnityContainer -> IUnityContainer 
#### Параметры
container IUnityContainer
    Контейнер, в котором выполняется регистрация.
#### Возвращаемое значение
IUnityContainer  
Контейнер container для цепочки вызовов.
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
[EDSExtensions - ](T_Tessa_EDS_EDSExtensions.htm)
[Tessa.EDS - пространство имён](N_Tessa_EDS.htm)
