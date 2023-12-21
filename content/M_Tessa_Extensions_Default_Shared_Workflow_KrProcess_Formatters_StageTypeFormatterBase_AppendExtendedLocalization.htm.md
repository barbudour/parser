# StageTypeFormatterBase.AppendExtendedLocalization - метод
Добавляет указанную строку в формате расширенной локализации, если она
является строкой локализации.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void AppendExtendedLocalization(
    	StringBuilder sb,
    	string str
    )
VB __Копировать
     Protected Shared Sub AppendExtendedLocalization ( 
    	sb As StringBuilder,
    	str As String
    )
C++ __Копировать
     protected:
    static void AppendExtendedLocalization(
    	StringBuilder^ sb, 
    	String^ str
    )
F# __Копировать
     static member AppendExtendedLocalization : 
            sb : StringBuilder * 
            str : string -> unit 
#### Параметры
sb
[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)
    Объект, используемый для построения строки.
str [String](https://learn.microsoft.com/dotnet/api/system.string)
    Строка, которая должна быть добавлена в формате расширенной локализации, если она является строкой локализации. Если строка не является строкой локализации, то она добавляется без изменений. Может иметь значение null.
##  __См. также
#### Ссылки
[StageTypeFormatterBase -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterBase.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)
