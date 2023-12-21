# ExtensionExtensions.WithInstance - метод
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством заданной ссылки на этот экземпляр. Проверка интерфейса
[IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm) не
выполняется, вы можете вызвать асинхронную инициализацию перед тем, как
передать экземпляр расширения в этот метод.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WithInstance(
    	this IExtensionPolicyContainer policyContainer,
    	IExtension instance
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WithInstance ( 
    	policyContainer As IExtensionPolicyContainer,
    	instance As IExtension
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WithInstance(
    	IExtensionPolicyContainer^ policyContainer, 
    	IExtension^ instance
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WithInstance : 
            policyContainer : IExtensionPolicyContainer * 
            instance : IExtension -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
instance [IExtension](T_Tessa_Extensions_IExtension.htm)
    Ссылка на экземпляр расширения.
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
