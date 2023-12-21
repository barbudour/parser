# StorageMappingResolverExtensions.RegisterKrStorageMappingHandlers - метод
Выполняет регистрацию типов для
[IStorageMappingResolver](T_Tessa_Platform_Storage_Mapping_IStorageMappingResolver.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.StorageMapping.StorageMappingHandlers](N_Tessa_Extensions_Default_Shared_StorageMapping_StorageMappingHandlers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static IResolver<Guid, IStorageMappingHandler> RegisterKrStorageMappingHandlers(
    	this IStorageMappingResolver storageMappingResolver
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function RegisterKrStorageMappingHandlers ( 
    	storageMappingResolver As IStorageMappingResolver
    ) As IResolver(Of Guid, IStorageMappingHandler)
C++ __Копировать
     public:
    [ExtensionAttribute]
    static IResolver<Guid, IStorageMappingHandler^>^ RegisterKrStorageMappingHandlers(
    	IStorageMappingResolver^ storageMappingResolver
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member RegisterKrStorageMappingHandlers : 
            storageMappingResolver : IStorageMappingResolver -> IResolver<Guid, IStorageMappingHandler> 
#### Параметры
storageMappingResolver
[IStorageMappingResolver](T_Tessa_Platform_Storage_Mapping_IStorageMappingResolver.htm)
    [IStorageMappingResolver](T_Tessa_Platform_Storage_Mapping_IStorageMappingResolver.htm).
#### Возвращаемое значение
[IResolver](T_Tessa_Platform_IResolver_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[IStorageMappingHandler](T_Tessa_Platform_Storage_Mapping_IStorageMappingHandler.htm)>  
Объект storageMappingResolver для цепочки вызовов.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[IStorageMappingResolver](T_Tessa_Platform_Storage_Mapping_IStorageMappingResolver.htm).
При вызове метода для экземпляра следует опускать первый параметр.
Дополнительные сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[StorageMappingResolverExtensions -
](T_Tessa_Extensions_Default_Shared_StorageMapping_StorageMappingHandlers_StorageMappingResolverExtensions.htm)
[Tessa.Extensions.Default.Shared.StorageMapping.StorageMappingHandlers -
пространство
имён](N_Tessa_Extensions_Default_Shared_StorageMapping_StorageMappingHandlers.htm)
