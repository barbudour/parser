# DocumentNumberDirector.FormatSequenceNameAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Numbers](N_Tessa_Extensions_Default_Shared_Numbers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected override Task<string> FormatSequenceNameAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	string formatString = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function FormatSequenceNameAsync ( 
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
    ) override
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
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
formatString [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __См. также
#### Ссылки
[DocumentNumberDirector -
](T_Tessa_Extensions_Default_Shared_Numbers_DocumentNumberDirector.htm)
[Tessa.Extensions.Default.Shared.Numbers - пространство
имён](N_Tessa_Extensions_Default_Shared_Numbers.htm)
