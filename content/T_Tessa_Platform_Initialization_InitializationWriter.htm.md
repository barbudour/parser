# InitializationWriter - класс
Объект, выполняющий запись в поток данных по инициализации.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class InitializationWriter : SerializableObjectWriter
VB __Копировать
     Public NotInheritable Class InitializationWriter
    	Inherits SerializableObjectWriter
C++ __Копировать
     public ref class InitializationWriter sealed : public SerializableObjectWriter
F# __Копировать
     [<SealedAttribute>]
    type InitializationWriter = 
        class
            inherit SerializableObjectWriter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SerializableObjectWriter](T_Tessa_Platform_IO_SerializableObjectWriter.htm) __ InitializationWriter
##  __Конструкторы
[InitializationWriter](M_Tessa_Platform_Initialization_InitializationWriter__ctor.htm)|
Создаёт экземпляр класса с указанием потока, в который будет выполняться
запись сериализуемых объектов.  
---|---  
## __Свойства
[Format](P_Tessa_Platform_IO_SerializableObjectWriter_Format.htm)|  Формат
сериализации.  
(Унаследован от
[SerializableObjectWriter](T_Tessa_Platform_IO_SerializableObjectWriter.htm))  
---|---  
[Stream](P_Tessa_Platform_IO_SerializableObjectWriter_Stream.htm)|  Поток, в
который выполняется запись данных.  
(Унаследован от
[SerializableObjectWriter](T_Tessa_Platform_IO_SerializableObjectWriter.htm))  
[StreamWriter](P_Tessa_Platform_IO_SerializableObjectWriter_StreamWriter.htm)|
Объект, выполняющий запись данных в поток
[Stream](P_Tessa_Platform_IO_SerializableObjectWriter_Stream.htm).  
(Унаследован от
[SerializableObjectWriter](T_Tessa_Platform_IO_SerializableObjectWriter.htm))  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WriteAsync](M_Tessa_Platform_IO_SerializableObjectWriter_WriteAsync.htm)|
Записывает все данные из заданного потока в агрегированный поток.  
(Унаследован от
[SerializableObjectWriter](T_Tessa_Platform_IO_SerializableObjectWriter.htm))  
[WriteObjectAsync(ISerializableObject,
CancellationToken)](M_Tessa_Platform_IO_SerializableObjectWriter_WriteObjectAsync.htm)|
Выполняет запись сериализуемого объекта в поток.  
(Унаследован от
[SerializableObjectWriter](T_Tessa_Platform_IO_SerializableObjectWriter.htm))  
[WriteObjectAsync(IStorageObjectProvider,
CancellationToken)](M_Tessa_Platform_IO_SerializableObjectWriter_WriteObjectAsync_1.htm)|
Выполняет запись сериализуемого объекта в поток.  
(Унаследован от
[SerializableObjectWriter](T_Tessa_Platform_IO_SerializableObjectWriter.htm))  
[WriteResponseAsync](M_Tessa_Platform_Initialization_InitializationWriter_WriteResponseAsync.htm)|
Записывает в потоке данных по инициализации ответ на запрос на инициализацию
приложения.  
## __Методы расширения
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
