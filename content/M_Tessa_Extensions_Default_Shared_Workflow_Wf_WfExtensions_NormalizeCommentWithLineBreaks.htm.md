# WfExtensions.NormalizeCommentWithLineBreaks - метод
Возвращает нормализованное значение комментария, в котором возможны переводы
строк в середине сообщения, но заменены и множественные пробелы на одиночные
пробелы, а также удалены пробелы и переводы строк по краям строки. Комментарий
при этом не усекается по длине.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.Wf](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static string NormalizeCommentWithLineBreaks(
    	this string comment
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function NormalizeCommentWithLineBreaks ( 
    	comment As String
    ) As String
C++ __Копировать
     public:
    [ExtensionAttribute]
    static String^ NormalizeCommentWithLineBreaks(
    	String^ comment
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member NormalizeCommentWithLineBreaks : 
            comment : string -> string 
#### Параметры
comment [String](https://learn.microsoft.com/dotnet/api/system.string)
    Комментарий, который необходимо нормализовать. Может быть равен null.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Нормализованное значение комментария с переводами строк.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [String](https://learn.microsoft.com/dotnet/api/system.string).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[WfExtensions -
](T_Tessa_Extensions_Default_Shared_Workflow_Wf_WfExtensions.htm)
[Tessa.Extensions.Default.Shared.Workflow.Wf - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_Wf.htm)
