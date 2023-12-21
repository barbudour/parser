# NumberBuilder.GetFullNumberCoreAsync - метод
Возвращает текстовое представление номера по числовому представлению для
заданного действия с номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<string> GetFullNumberCoreAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	long number,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function GetFullNumberCoreAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	number As Long,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of String)
C++ __Копировать
     protected:
    virtual Task<String^>^ GetFullNumberCoreAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	long long number, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetFullNumberCoreAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            number : int64 * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
    override GetFullNumberCoreAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            number : int64 * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст действия номером.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип номера.
number [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
    Числовое представление номера.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Текстовое представление номера.
##  __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
