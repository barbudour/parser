# ExtensionExtensions.ResolveAssemblyInfo - метод
Получает объект
[IExtensionAssemblyInfo](T_Tessa_Extensions_IExtensionAssemblyInfo.htm) с
информацией по сборкам из контейнера Unity. Если объект не зарегистрирован, то
создаёт новый объект, регистрирует его и возвращает.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionAssemblyInfo ResolveAssemblyInfo(
    	this IUnityContainer unityContainer
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ResolveAssemblyInfo ( 
    	unityContainer As IUnityContainer
    ) As IExtensionAssemblyInfo
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionAssemblyInfo^ ResolveAssemblyInfo(
    	IUnityContainer^ unityContainer
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ResolveAssemblyInfo : 
            unityContainer : IUnityContainer -> IExtensionAssemblyInfo 
#### Параметры
unityContainer IUnityContainer
    Контейнер Unity.
#### Возвращаемое значение
[IExtensionAssemblyInfo](T_Tessa_Extensions_IExtensionAssemblyInfo.htm)  
Объект [IExtensionAssemblyInfo](T_Tessa_Extensions_IExtensionAssemblyInfo.htm)
с информацией по сборкам.
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
[ExtensionExtensions - ](T_Tessa_Extensions_ExtensionExtensions.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
