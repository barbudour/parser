# ExtensionExtensions.WithDefaultConstructor - метод
Регистрирует политику, указывающую на способ получения экземпляров расширений
посредством их конструкторов по умолчанию. Если класс расширения реализует
интерфейс [IAsyncInitializable](T_Tessa_Platform_IAsyncInitializable.htm), то
для каждого созданного экземпляра будет вызвана асинхронная инициализация.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IExtensionPolicyContainer WithDefaultConstructor(
    	this IExtensionPolicyContainer policyContainer
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function WithDefaultConstructor ( 
    	policyContainer As IExtensionPolicyContainer
    ) As IExtensionPolicyContainer
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IExtensionPolicyContainer^ WithDefaultConstructor(
    	IExtensionPolicyContainer^ policyContainer
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WithDefaultConstructor : 
            policyContainer : IExtensionPolicyContainer -> IExtensionPolicyContainer 
#### Параметры
policyContainer
[IExtensionPolicyContainer](T_Tessa_Extensions_IExtensionPolicyContainer.htm)
    Контейнер политик, ассоциированных с расширениями.
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
