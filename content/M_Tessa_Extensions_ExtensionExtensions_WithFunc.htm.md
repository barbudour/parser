# ExtensionExtensions.WithFunc - метод
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством заданной функции. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию непосредственно
внутри функции.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WithFunc(
    	this IExtensionPolicyContainer policyContainer,
    	Func<ExtensionBuildKey, ExtensionResolveKey, CancellationToken, ValueTask<IExtension>> resolveFunc
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WithFunc ( 
    	policyContainer As IExtensionPolicyContainer,
    	resolveFunc As Func(Of ExtensionBuildKey, ExtensionResolveKey, CancellationToken, ValueTask(Of IExtension))
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WithFunc(
    	IExtensionPolicyContainer^ policyContainer, 
    	Func<ExtensionBuildKey^, ExtensionResolveKey^, CancellationToken, ValueTask<IExtension^>>^ resolveFunc
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WithFunc : 
            policyContainer : IExtensionPolicyContainer * 
            resolveFunc : Func<ExtensionBuildKey, ExtensionResolveKey, CancellationToken, ValueTask<IExtension>> -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
resolveFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-4)<[ExtensionBuildKey](T_Tessa_Extensions_ExtensionBuildKey.htm),
[ExtensionResolveKey](T_Tessa_Extensions_ExtensionResolveKey.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IExtension](T_Tessa_Extensions_IExtension.htm)>>
    Функция, используемая для получения экземпляра расширения.
#### Возвращаемое значение
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)  
Заданный контейнер policyContainer для цепочки вызовов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[ExtensionExtensions - ](T_Tessa_Extensions_ExtensionExtensions.htm)
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
