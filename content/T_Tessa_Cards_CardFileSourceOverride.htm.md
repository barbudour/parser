# CardFileSourceOverride - класс
Настройки по местоположению контента файла
[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardFileSourceOverride : StorageSerializable, 
    	ICardFileSourceOverride, IStorageSerializable, ISealable
VB __Копировать
     Public NotInheritable Class CardFileSourceOverride
    	Inherits StorageSerializable
    	Implements ICardFileSourceOverride, IStorageSerializable, ISealable
C++ __Копировать
     public ref class CardFileSourceOverride sealed : public StorageSerializable, 
    	ICardFileSourceOverride, IStorageSerializable, ISealable
F# __Копировать
     [<SealedAttribute>]
    type CardFileSourceOverride = 
        class
            inherit StorageSerializable
            interface ICardFileSourceOverride
            interface IStorageSerializable
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __ CardFileSourceOverride
Implements
    [ICardFileSourceOverride](T_Tessa_Cards_ICardFileSourceOverride.htm), [ISealable](T_Tessa_Platform_ISealable.htm), [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Конструкторы
[CardFileSourceOverride](M_Tessa_Cards_CardFileSourceOverride__ctor.htm)|
Инициализирует новый экземпляр класса CardFileSourceOverride  
---|---  
##  __Свойства
[FileExtensions](P_Tessa_Cards_CardFileSourceOverride_FileExtensions.htm)|
Список рекомендуемый расширений для использования совместно с этим источником
файла.  
---|---  
[ID](P_Tessa_Cards_CardFileSourceOverride_ID.htm)|  Идентификатор
местоположения файлов.  
[IsDatabase](P_Tessa_Cards_CardFileSourceOverride_IsDatabase.htm)|  Признак
того, что местоположение соответствует базе данных, а не файловой папке.  
[IsSealed](P_Tessa_Cards_CardFileSourceOverride_IsSealed.htm)| Признак того,
что объект был защищён от изменений.  
[MaxSize](P_Tessa_Cards_CardFileSourceOverride_MaxSize.htm)|  Максимальный
размер занятого места в местоположении. Не заполняется и не используется
системой, возможно использование в расширениях.  
[Name](P_Tessa_Cards_CardFileSourceOverride_Name.htm)|  Отображаемое имя
местоположения.  
[Path](P_Tessa_Cards_CardFileSourceOverride_Path.htm)|  Путь к местоположению.
Соответвует имени строки подключения к БД из конфигурационного файла или
полному путь к файловой папке.  
[Size](P_Tessa_Cards_CardFileSourceOverride_Size.htm)|  Текущий размер
занятого места в байтах в местоположении. Не заполняется и не используется
системой, возможно использование в расширениях.  
[UseSimpleNamingScheme](P_Tessa_Cards_CardFileSourceOverride_UseSimpleNamingScheme.htm)|
Признак того, что используется упрощённая схема именования папок, где для
карточек не создаются дополнительные подпапки. Значение true не рекомендуется,
если в системе возможны миллионы карточек с файлами, т.к. это приведёт к
миллионам подпапок внутри одной папки в файловой системе. Значение неактуально
для файлов в базе данных.  
## __Методы
[Apply](M_Tessa_Cards_CardFileSourceOverride_Apply.htm)|  Применяет изменения
для указанного объекта, и возвращает его изменённую копию.  
---|---  
[Deserialize](M_Tessa_Platform_Storage_StorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeAndGetCore](M_Tessa_Platform_Storage_StorageSerializable_DeserializeAndGetCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeCore](M_Tessa_Cards_CardFileSourceOverride_DeserializeCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Переопределяет [StorageSerializable.DeserializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_DeserializeCore.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Seal](M_Tessa_Cards_CardFileSourceOverride_Seal.htm)| Защищает объект от
изменений.  
[Serialize](M_Tessa_Platform_Storage_StorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[SerializeCore](M_Tessa_Cards_CardFileSourceOverride_SerializeCore.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Переопределяет [StorageSerializable.SerializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_SerializeCore.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToSerializedDictionary](M_Tessa_Platform_Storage_StorageExtensions_ToSerializedDictionary.htm)|
Сериализует объект в нетипизированный словарь.  
(Определяется
[StorageExtensions](T_Tessa_Platform_Storage_StorageExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
