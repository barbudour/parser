# ApplicationsPipesExtensions.CreateApplicationsServiceRouter - метод
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Pipes](N_Tessa_Applications_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IPipeRouter CreateApplicationsServiceRouter(
    	this IPipeRouteFactory routeFactory,
    	IPipeInstanceResolver instanceResolver
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function CreateApplicationsServiceRouter ( 
    	routeFactory As IPipeRouteFactory,
    	instanceResolver As IPipeInstanceResolver
    ) As IPipeRouter
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IPipeRouter^ CreateApplicationsServiceRouter(
    	IPipeRouteFactory^ routeFactory, 
    	IPipeInstanceResolver^ instanceResolver
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member CreateApplicationsServiceRouter : 
            routeFactory : IPipeRouteFactory * 
            instanceResolver : IPipeInstanceResolver -> IPipeRouter 
#### Параметры
routeFactory [IPipeRouteFactory](T_Tessa_Platform_Pipes_IPipeRouteFactory.htm)
instanceResolver
[IPipeInstanceResolver](T_Tessa_Platform_Pipes_IPipeInstanceResolver.htm)
#### Возвращаемое значение
[IPipeRouter](T_Tessa_Platform_Pipes_IPipeRouter.htm)
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IPipeRouteFactory](T_Tessa_Platform_Pipes_IPipeRouteFactory.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[ApplicationsPipesExtensions -
](T_Tessa_Applications_Pipes_ApplicationsPipesExtensions.htm)
[Tessa.Applications.Pipes - пространство имён](N_Tessa_Applications_Pipes.htm)
