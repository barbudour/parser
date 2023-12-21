# StageTypeFormatterBase.AppendString - метод
Добавляет форматированную строку с описанием настройки этапа в builder.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected static void AppendString(
    	StringBuilder builder,
    	string value,
    	string caption,
    	bool localizable = false,
    	bool canBeWithoutValue = false,
    	int limit = -1,
    	bool appendNewLine = true
    )
VB __Копировать
     Protected Shared Sub AppendString ( 
    	builder As StringBuilder,
    	value As String,
    	caption As String,
    	Optional localizable As Boolean = false,
    	Optional canBeWithoutValue As Boolean = false,
    	Optional limit As Integer = -1,
    	Optional appendNewLine As Boolean = true
    )
C++ __Копировать
     protected:
    static void AppendString(
    	StringBuilder^ builder, 
    	String^ value, 
    	String^ caption, 
    	bool localizable = false, 
    	bool canBeWithoutValue = false, 
    	int limit = -1, 
    	bool appendNewLine = true
    )
F# __Копировать
     static member AppendString : 
            builder : StringBuilder * 
            value : string * 
            caption : string * 
            ?localizable : bool * 
            ?canBeWithoutValue : bool * 
            ?limit : int * 
            ?appendNewLine : bool 
    (* Defaults:
            let _localizable = defaultArg localizable false
            let _canBeWithoutValue = defaultArg canBeWithoutValue false
            let _limit = defaultArg limit -1
            let _appendNewLine = defaultArg appendNewLine true
    *)
    -> unit 
#### Параметры
builder
[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)
    Конструктор строки.
value [String](https://learn.microsoft.com/dotnet/api/system.string)
    Значение параметра.
caption [String](https://learn.microsoft.com/dotnet/api/system.string)
    Заголовок (название) добавляемой колонки. Может быть строкой локализации вида "$LocalizationString". Может быть не задано.
localizable [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Необходимо локализовать значение настройки.
canBeWithoutValue
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
    Значение true, если требуется добавить заголовок (название) параметра, если значение параметра равно null, [Empty](https://learn.microsoft.com/dotnet/api/system.string.empty) или состоит из одних символов пробела.
limit [Int32](https://learn.microsoft.com/dotnet/api/system.int32) (Optional)
     Максимальная длина строки со значением параметра. -1, если значение не ограничено. 
appendNewLine [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Значение true, если перед добавляемой строкой должен быть добавлен знак завершения строки по умолчанию, иначе - false. Перевод строки добавляется только, если builder содержит данные.
##  __См. также
#### Ссылки
[StageTypeFormatterBase -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters_StageTypeFormatterBase.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess.Formatters - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess_Formatters.htm)
