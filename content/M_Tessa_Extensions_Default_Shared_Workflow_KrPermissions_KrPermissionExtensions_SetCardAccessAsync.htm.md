# KrPermissionExtensions.SetCardAccessAsync(ICardExtensionContext, String,
ICollection<String>) - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task SetCardAccessAsync(
    	this ICardExtensionContext context,
    	string section,
    	ICollection<string> fields
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function SetCardAccessAsync ( 
    	context As ICardExtensionContext,
    	section As String,
    	fields As ICollection(Of String)
    ) As Task
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task^ SetCardAccessAsync(
    	ICardExtensionContext^ context, 
    	String^ section, 
    	ICollection<String^>^ fields
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member SetCardAccessAsync : 
            context : ICardExtensionContext * 
            section : string * 
            fields : ICollection<string> -> Task 
#### Параметры
context
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm)
section [String](https://learn.microsoft.com/dotnet/api/system.string)
fields
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[ICardExtensionContext](T_Tessa_Cards_Extensions_ICardExtensionContext.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[KrPermissionExtensions -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionExtensions.htm)
[SetCardAccessAsync -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionExtensions_SetCardAccessAsync.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)
