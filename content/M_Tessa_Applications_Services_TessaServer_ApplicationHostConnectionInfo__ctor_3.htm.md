# ApplicationHostConnectionInfo(IStorageObjectProvider) - конструктор
Создаёт экземпляр класса с указанием объекта, предоставляющего доступ к
хранилищу, декоратором для которого является создаваемый объект.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationHostConnectionInfo(
    	IStorageObjectProvider storageProvider
    )
VB __Копировать
     Public Sub New ( 
    	storageProvider As IStorageObjectProvider
    )
C++ __Копировать
     public:
    ApplicationHostConnectionInfo(
    	IStorageObjectProvider^ storageProvider
    )
F# __Копировать
     new : 
            storageProvider : IStorageObjectProvider -> ApplicationHostConnectionInfo
#### Параметры
storageProvider
[IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm)
     Объект, предоставляющий доступ к хранилищу Dictionary<string, object>, декоратором для которого является создаваемый объект. 
## __См. также
#### Ссылки
[ApplicationHostConnectionInfo -
](T_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo.htm)
[ApplicationHostConnectionInfo -
перегрузка](Overload_Tessa_Applications_Services_TessaServer_ApplicationHostConnectionInfo__ctor.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
