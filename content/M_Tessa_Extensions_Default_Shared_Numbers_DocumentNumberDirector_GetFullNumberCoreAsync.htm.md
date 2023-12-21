# DocumentNumberDirector.GetFullNumberCoreAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Numbers](N_Tessa_Extensions_Default_Shared_Numbers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected override Task<string> GetFullNumberCoreAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	long number,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function GetFullNumberCoreAsync ( 
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
    ) override
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
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
number [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
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
