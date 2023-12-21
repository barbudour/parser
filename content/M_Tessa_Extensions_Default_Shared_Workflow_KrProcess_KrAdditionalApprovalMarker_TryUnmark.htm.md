# KrAdditionalApprovalMarker.TryUnmark - метод
Удаляет метку о доп. согласующих из указанной строки, если она присутствует.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool TryUnmark(
    	string str,
    	out string resultStr
    )
VB __Копировать
     Public Shared Function TryUnmark ( 
    	str As String,
    	<OutAttribute> ByRef resultStr As String
    ) As Boolean
C++ __Копировать
     public:
    static bool TryUnmark(
    	String^ str, 
    	[OutAttribute] String^% resultStr
    )
F# __Копировать
     static member TryUnmark : 
            str : string * 
            resultStr : string byref -> bool 
#### Параметры
str [String](https://learn.microsoft.com/dotnet/api/system.string)
    Строка из которой требуется удалить метку.
resultStr [String](https://learn.microsoft.com/dotnet/api/system.string)
    Результирующая строка.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Значение true, если строка была изменена, иначе - false.
##  __См. также
#### Ссылки
[KrAdditionalApprovalMarker -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrAdditionalApprovalMarker.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
