# IApplicationServiceLegacy.ResolveFailResult - метод
Возвращает ошибки при скачивании приложения как объект [!:ValidationResult],
сериализованный в виде массива байт, или null, либо пустой массив, если
информация недоступна: ошибок не было или пользователь не имеет доступа к этой
записи в истории.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [CanBeNullAttribute]
    [OperationContractAttribute]
    byte[] ResolveFailResult(
    	Guid rowID
    )
VB __Копировать
    <CanBeNullAttribute>
    <OperationContractAttribute>
    Function ResolveFailResult ( 
    	rowID As Guid
    ) As Byte()
C++ __Копировать
    [CanBeNullAttribute]
    [OperationContractAttribute]
    array<unsigned char>^ ResolveFailResult(
    	Guid rowID
    )
F# __Копировать
     [<CanBeNullAttribute>]
    [<OperationContractAttribute>]
    abstract ResolveFailResult : 
            rowID : Guid -> byte[] 
#### Параметры
rowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор записи в истории, которая возвращается в свойстве [ActionHistoryRowID](P_Tessa_Applications_Package_ApplicationPackage_ActionHistoryRowID.htm) для загруженного пакета.
#### Возвращаемое значение
[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]  
Массив байт с сериализованным объектом [!:ValidationResult], или null, либо
пустой массив, если информация по ошибке скачивания недоступна.
## __См. также
#### Ссылки
[IApplicationServiceLegacy -
](T_Tessa_Applications_Services_TessaServer_IApplicationServiceLegacy.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
