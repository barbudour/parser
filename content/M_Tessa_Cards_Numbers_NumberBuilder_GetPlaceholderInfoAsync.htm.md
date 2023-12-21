# NumberBuilder.GetPlaceholderInfoAsync - метод
Создаёт или возвращает объект с дополнительной информацией, необходимой при
обращении к API плейсхолдеров. Созданный объект кэшируется в контексте
context, чтобы для той же операции он мог повторно использоваться. Например,
если в операции форматируются и имя последовательности, и строковое
представление номера, то обе операции по форматированию получат один и тот же
объект с дополнительной информацией.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<Dictionary<string, Object>> GetPlaceholderInfoAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	string formatString,
    	long? number = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function GetPlaceholderInfoAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	formatString As String,
    	Optional number As Long? = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Dictionary(Of String, Object))
C++ __Копировать
     protected:
    virtual ValueTask<Dictionary<String^, Object^>^> GetPlaceholderInfoAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	String^ formatString, 
    	Nullable<long long> number = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetPlaceholderInfoAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            formatString : string * 
            ?number : Nullable<int64> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _number = defaultArg number null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Dictionary<string, Object>> 
    override GetPlaceholderInfoAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            formatString : string * 
            ?number : Nullable<int64> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _number = defaultArg number null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Dictionary<string, Object>> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип номера.
formatString [String](https://learn.microsoft.com/dotnet/api/system.string)
     Строка форматирования для номера. Если указаны null или пустая строка, то выполняется форматирование номера по умолчанию. 
number
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
(Optional)
    Числовое представление номера.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>>  
Объект с дополнительной информацией, необходимой при обращении к API
плейсхолдеров.
##  __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
