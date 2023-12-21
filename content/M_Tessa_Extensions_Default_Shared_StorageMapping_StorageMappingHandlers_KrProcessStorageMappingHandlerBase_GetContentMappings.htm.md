# KrProcessStorageMappingHandlerBase.GetContentMappings - метод
Получает параметры сериализации для выгрузки контента карточек во внешние
файлы.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.StorageMapping.StorageMappingHandlers](N_Tessa_Extensions_Default_Shared_StorageMapping_StorageMappingHandlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual IList<IStorageContentMapping> GetContentMappings(
    	Card card
    )
VB __Копировать
     Public Overridable Function GetContentMappings ( 
    	card As Card
    ) As IList(Of IStorageContentMapping)
C++ __Копировать
     public:
    virtual IList<IStorageContentMapping^>^ GetContentMappings(
    	Card^ card
    )
F# __Копировать
     abstract GetContentMappings : 
            card : Card -> IList<IStorageContentMapping> 
    override GetContentMappings : 
            card : Card -> IList<IStorageContentMapping> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Объект карточки, для которой необходимо получить параметры сериализации.
#### Возвращаемое значение
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IStorageContentMapping](T_Tessa_Platform_Storage_IStorageContentMapping.htm)>  
Параметры сериализации для выгрузки контента карточек во внешние файлы.
#### Реализации
[IStorageMappingHandler.GetContentMappings(Card)](M_Tessa_Platform_Storage_Mapping_IStorageMappingHandler_GetContentMappings.htm)  
##  __См. также
#### Ссылки
[KrProcessStorageMappingHandlerBase -
](T_Tessa_Extensions_Default_Shared_StorageMapping_StorageMappingHandlers_KrProcessStorageMappingHandlerBase.htm)
[Tessa.Extensions.Default.Shared.StorageMapping.StorageMappingHandlers -
пространство
имён](N_Tessa_Extensions_Default_Shared_StorageMapping_StorageMappingHandlers.htm)
