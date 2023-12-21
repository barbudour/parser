# NumberBuilder.FormatNumberAsync - метод
Форматирует текстовое представление номера по заданной строке форматирования.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<string> FormatNumberAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	long number,
    	string formatString = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function FormatNumberAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	number As Long,
    	Optional formatString As String = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of String)
C++ __Копировать
     protected:
    virtual Task<String^>^ FormatNumberAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	long long number, 
    	String^ formatString = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract FormatNumberAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            number : int64 * 
            ?formatString : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _formatString = defaultArg formatString null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
    override FormatNumberAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            number : int64 * 
            ?formatString : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _formatString = defaultArg formatString null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип номера.
number [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
    Числовое представление номера.
formatString [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Строка форматирования для номера. Если указаны null или пустая строка, то выполняется форматирование номера по умолчанию. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Текстовое представление номера, полученное для заданной строки форматирования.
##  __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
