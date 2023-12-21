# DocumentNumberDirector.TryGetSequenceNameCoreAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Numbers](N_Tessa_Extensions_Default_Shared_Numbers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected override Task<string> TryGetSequenceNameCoreAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function TryGetSequenceNameCoreAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of String)
C++ __Копировать
     protected:
    virtual Task<String^>^ TryGetSequenceNameCoreAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract TryGetSequenceNameCoreAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
    override TryGetSequenceNameCoreAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<string> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
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
