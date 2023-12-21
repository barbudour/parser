# CardGetFileVersionStorageCompressor - класс
Выполняет упаковку или распаковку списка версий в объекте
[CardGetFileVersionsResponse](T_Tessa_Cards_CardGetFileVersionsResponse.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardGetFileVersionStorageCompressor : IStorageCompressor
VB __Копировать
     Public NotInheritable Class CardGetFileVersionStorageCompressor
    	Implements IStorageCompressor
C++ __Копировать
     public ref class CardGetFileVersionStorageCompressor sealed : IStorageCompressor
F# __Копировать
     [<SealedAttribute>]
    type CardGetFileVersionStorageCompressor = 
        class
            interface IStorageCompressor
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardGetFileVersionStorageCompressor
Implements
    [IStorageCompressor](T_Tessa_Platform_Storage_IStorageCompressor.htm)
##  __Заметки
Упакованный список версий в объекте становится непригоден для использования
посредством декораторов.
Экземпляр этого класса является неизменяемым после своего создания, а все его
методы являются потокобезопасными.
##  __Конструкторы
[CardGetFileVersionStorageCompressor](M_Tessa_Cards_CardGetFileVersionStorageCompressor__ctor.htm)|
Создаёт экземпляр класса с указанием объектов, используемых для упаковки и
распаковки версий файлов карточки.  
---|---  
## __Свойства
[Default](P_Tessa_Cards_CardGetFileVersionStorageCompressor_Default.htm)|
Экземпляр класса.  
---|---  
##  __Методы
[Compress](M_Tessa_Cards_CardGetFileVersionStorageCompressor_Compress.htm)|
Выполняет упаковку данных, располагающихся в хранилище storage по ключу
targetKey.  
---|---  
[Decompress](M_Tessa_Cards_CardGetFileVersionStorageCompressor_Decompress.htm)|
Выполняет распаковку данных, располагающихся в хранилище storage по ключу
targetKey. Данные должны быть запакованы этим же или совместимым объектом
[Tessa.Platform.Storage.IStorageCompressor].  
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
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
