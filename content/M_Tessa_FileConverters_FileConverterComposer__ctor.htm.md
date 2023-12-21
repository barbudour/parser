# FileConverterComposer - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileConverterComposer(
    	IFileConverterCache fileConverterCache,
    	IOperationRepository operationRepository,
    	IDbScope dbScope,
    	ISignatureProvider signatureProvider = null
    )
VB __Копировать
     Public Sub New ( 
    	fileConverterCache As IFileConverterCache,
    	operationRepository As IOperationRepository,
    	dbScope As IDbScope,
    	Optional signatureProvider As ISignatureProvider = Nothing
    )
C++ __Копировать
     public:
    FileConverterComposer(
    	IFileConverterCache^ fileConverterCache, 
    	IOperationRepository^ operationRepository, 
    	IDbScope^ dbScope, 
    	ISignatureProvider^ signatureProvider = nullptr
    )
F# __Копировать
     new : 
            fileConverterCache : IFileConverterCache * 
            operationRepository : IOperationRepository * 
            dbScope : IDbScope * 
            ?signatureProvider : ISignatureProvider 
    (* Defaults:
            let _signatureProvider = defaultArg signatureProvider null
    *)
    -> FileConverterComposer
#### Параметры
fileConverterCache
[IFileConverterCache](T_Tessa_FileConverters_IFileConverterCache.htm)
     Объект, обеспечивающий кэширование файлов, преобразованных из одного формата в другой. 
operationRepository
[IOperationRepository](T_Tessa_Platform_Operations_IOperationRepository.htm)
    Репозиторий, управляющий операциями.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
    Объект, обеспечивающий доступ к базе данных.
signatureProvider
[ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm) (Optional)
     Объект, используемый для вычисления хеша запроса. Рекомендуется получить объект по имени [Operations](F_Tessa_Platform_SignatureProviderNames_Operations.htm). Если указано null, то используется провайдер по умолчанию [!:SyncSignatureProvider.Operations]. 
## __См. также
#### Ссылки
[FileConverterComposer - ](T_Tessa_FileConverters_FileConverterComposer.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
