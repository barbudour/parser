# ICardFileSourceOverride - интерфейс
Настройки по местоположению контента файла
[ICardFileSource](T_Tessa_Cards_ICardFileSource.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardFileSourceOverride : IStorageSerializable, 
    	ISealable
VB __Копировать
     Public Interface ICardFileSourceOverride
    	Inherits IStorageSerializable, ISealable
C++ __Копировать
     public interface class ICardFileSourceOverride : IStorageSerializable, 
    	ISealable
F# __Копировать
     type ICardFileSourceOverride = 
        interface
            interface IStorageSerializable
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm)
##  __Свойства
[FileExtensions](P_Tessa_Cards_ICardFileSourceOverride_FileExtensions.htm)|
Список рекомендуемый расширений для использования совместно с этим источником
файла.  
---|---  
[ID](P_Tessa_Cards_ICardFileSourceOverride_ID.htm)|  Идентификатор
местоположения файлов.  
[IsDatabase](P_Tessa_Cards_ICardFileSourceOverride_IsDatabase.htm)|  Признак
того, что местоположение соответствует базе данных, а не файловой папке.  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[MaxSize](P_Tessa_Cards_ICardFileSourceOverride_MaxSize.htm)|  Максимальный
размер занятого места в местоположении. Не заполняется и не используется
системой, возможно использование в расширениях.  
[Name](P_Tessa_Cards_ICardFileSourceOverride_Name.htm)|  Отображаемое имя
местоположения.  
[Path](P_Tessa_Cards_ICardFileSourceOverride_Path.htm)|  Путь к
местоположению. Соответвует имени строки подключения к БД из конфигурационного
файла или полному путь к файловой папке.  
[Size](P_Tessa_Cards_ICardFileSourceOverride_Size.htm)|  Текущий размер
занятого места в байтах в местоположении. Не заполняется и не используется
системой, возможно использование в расширениях.  
[UseSimpleNamingScheme](P_Tessa_Cards_ICardFileSourceOverride_UseSimpleNamingScheme.htm)|
Признак того, что используется упрощённая схема именования папок, где для
карточек не создаются дополнительные подпапки. Значение true не рекомендуется,
если в системе возможны миллионы карточек с файлами, т.к. это приведёт к
миллионам подпапок внутри одной папки в файловой системе. Значение неактуально
для файлов в базе данных.  
## __Методы
[Apply](M_Tessa_Cards_ICardFileSourceOverride_Apply.htm)|  Применяет изменения
для указанного объекта, и возвращает его изменённую копию.  
---|---  
[Deserialize](M_Tessa_Platform_Storage_IStorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm))  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Serialize](M_Tessa_Platform_Storage_IStorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[IStorageSerializable](T_Tessa_Platform_Storage_IStorageSerializable.htm))  
##  __Методы расширения
[ToSerializedDictionary](M_Tessa_Platform_Storage_StorageExtensions_ToSerializedDictionary.htm)|
Сериализует объект в нетипизированный словарь.  
(Определяется
[StorageExtensions](T_Tessa_Platform_Storage_StorageExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
