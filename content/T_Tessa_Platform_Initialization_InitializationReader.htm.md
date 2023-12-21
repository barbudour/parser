# InitializationReader - класс
Объект, выполняющий чтение из потока данных по инициализации.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class InitializationReader : SerializableObjectReader
VB __Копировать
     Public NotInheritable Class InitializationReader
    	Inherits SerializableObjectReader
C++ __Копировать
     public ref class InitializationReader sealed : public SerializableObjectReader
F# __Копировать
     [<SealedAttribute>]
    type InitializationReader = 
        class
            inherit SerializableObjectReader
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SerializableObjectReader](T_Tessa_Platform_IO_SerializableObjectReader.htm) __ InitializationReader
##  __Конструкторы
[InitializationReader](M_Tessa_Platform_Initialization_InitializationReader__ctor.htm)|
Создаёт экземпляр класса с указанием потока, из которого будет выполняться
чтение сериализуемых объектов.  
---|---  
## __Свойства
[Format](P_Tessa_Platform_IO_SerializableObjectReader_Format.htm)|  Формат
сериализации.  
(Унаследован от
[SerializableObjectReader](T_Tessa_Platform_IO_SerializableObjectReader.htm))  
---|---  
[Stream](P_Tessa_Platform_IO_SerializableObjectReader_Stream.htm)|  Поток, из
которого выполняется чтение данных.  
(Унаследован от
[SerializableObjectReader](T_Tessa_Platform_IO_SerializableObjectReader.htm))  
[StreamReader](P_Tessa_Platform_IO_SerializableObjectReader_StreamReader.htm)|
Объект, выполняющий чтение данных из потока
[Stream](P_Tessa_Platform_IO_SerializableObjectReader_Stream.htm).  
(Унаследован от
[SerializableObjectReader](T_Tessa_Platform_IO_SerializableObjectReader.htm))  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[ReadObjectAsync](M_Tessa_Platform_IO_SerializableObjectReader_ReadObjectAsync.htm)|
Выполняет чтение сериализуемого объекта из потока.  
(Унаследован от
[SerializableObjectReader](T_Tessa_Platform_IO_SerializableObjectReader.htm))  
[ReadResponseAsync](M_Tessa_Platform_Initialization_InitializationReader_ReadResponseAsync.htm)|
Выполняет чтение из потока данных по инициализации ответ на запрос на
инициализацию приложения.  
[ReadStream](M_Tessa_Platform_IO_SerializableObjectReader_ReadStream.htm)|
Выполняет потоковое чтение данных, ограниченных заданным размером length.  
(Унаследован от
[SerializableObjectReader](T_Tessa_Platform_IO_SerializableObjectReader.htm))  
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
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
