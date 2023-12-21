# KrPermissionExtensions.TryGetServerToken - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static KrToken TryGetServerToken(
    	this IDictionary<string, Object> info
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function TryGetServerToken ( 
    	info As IDictionary(Of String, Object)
    ) As KrToken
C++ __Копировать
     public:
    [ExtensionAttribute]
    static KrToken^ TryGetServerToken(
    	IDictionary<String^, Object^>^ info
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member TryGetServerToken : 
            info : IDictionary<string, Object> -> KrToken 
#### Параметры
info
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
#### Возвращаемое значение
[KrToken](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken.htm)
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>. При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[KrPermissionExtensions -
](T_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionExtensions.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)
