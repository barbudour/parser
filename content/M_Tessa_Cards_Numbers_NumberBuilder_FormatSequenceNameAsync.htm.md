# NumberBuilder.FormatSequenceNameAsync - метод
Форматирует имя последовательности по заданной строке форматирования.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<string> FormatSequenceNameAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	string formatString = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function FormatSequenceNameAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	Optional formatString As String = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of String)
C++ __Копировать
     protected:
    virtual Task<String^>^ FormatSequenceNameAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	String^ formatString = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract FormatSequenceNameAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            ?formatString : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _formatString = defaultArg formatString null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
    override FormatSequenceNameAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
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
formatString [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Строка форматирования для имени последовательности. Если указаны null или пустая строка, то выполняется форматирование имени последовательности по умолчанию. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Имя последовательности, полученное для заданной строки форматирования.
##  __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
