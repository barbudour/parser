# ExtensionExtensions.WithOrder - метод
Регистрирует политику, указывающую порядок выполнения расширения в цепочке.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WithOrder(
    	this IExtensionPolicyContainer policyContainer,
    	ExtensionStage stage,
    	int order = 0
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WithOrder ( 
    	policyContainer As IExtensionPolicyContainer,
    	stage As ExtensionStage,
    	Optional order As Integer = 0
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WithOrder(
    	IExtensionPolicyContainer^ policyContainer, 
    	ExtensionStage stage, 
    	int order = 0
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WithOrder : 
            policyContainer : IExtensionPolicyContainer * 
            stage : ExtensionStage * 
            ?order : int 
    (* Defaults:
            let _order = defaultArg order 0
    *)
    -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
stage [ExtensionStage](T_Tessa_Extensions_ExtensionStage.htm)
    Этап выполнения расширения в цепочке расширений.
order [Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
     Порядок выполнения расширений внутри этапа. Расширения с меньшим значением порядка выполняются раньше. 
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
