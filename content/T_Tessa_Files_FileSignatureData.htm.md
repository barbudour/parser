# FileSignatureData - класс
Объект, содержащий информацию по бинарным данным файла подписи.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class FileSignatureData : NotificationObject, 
    	IFileSignatureData, INotifyPropertyChanged
VB __Копировать
     Public Class FileSignatureData
    	Inherits NotificationObject
    	Implements IFileSignatureData, INotifyPropertyChanged
C++ __Копировать
     public ref class FileSignatureData : public NotificationObject, 
    	IFileSignatureData, INotifyPropertyChanged
F# __Копировать
     type FileSignatureData = 
        class
            inherit NotificationObject
            interface IFileSignatureData
            interface INotifyPropertyChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[NotificationObject](T_Tessa_Platform_NotificationObject.htm) __ FileSignatureData
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IFileSignatureData](T_Tessa_Files_IFileSignatureData.htm)
##  __Заметки
Наследники класса могут переопределять методы и содержать дополнительные
свойства, связанные с внешней подсистемой, в которой располагается подписанная
версия.
## __Конструкторы
[FileSignatureData(FileSignatureDataState)](M_Tessa_Files_FileSignatureData__ctor_1.htm)|
Создаёт экземпляр класса без указания бинарных данных файла подписи в виде
массива байт.  
---|---  
[FileSignatureData(Byte[],
FileSignatureDataState)](M_Tessa_Files_FileSignatureData__ctor.htm)|  Создаёт
экземпляр класса с указанием бинарных данных файла подписи в виде массива
байт.  
## __Свойства
[Bytes](P_Tessa_Files_FileSignatureData_Bytes.htm)|  Массив байт с бинарными
данными файла подписи или null, если бинарные данные определяются другим
способом.  
---|---  
[IsEmpty](P_Tessa_Files_FileSignatureData_IsEmpty.htm)| Признак того, что
бинарные данные файла подписи не заполнены.  
[State](P_Tessa_Files_FileSignatureData_State.htm)| Состояние бинарных данных
файла подписи.  
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
[GetBytesAsync](M_Tessa_Files_FileSignatureData_GetBytesAsync.htm)|
Возвращает бинарные данные файла подписи в виде массива байт. Возвращённый
массив не равенnull.  
[GetBytesCoreAsync](M_Tessa_Files_FileSignatureData_GetBytesCoreAsync.htm)|
Возвращает бинарные данные файла подписи в виде массива байт. Возвращённый
массив не равенnull.  
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
[OnPropertyChanged(PropertyChangedEventArgs)](M_Tessa_Platform_NotificationObject_OnPropertyChanged.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChanged(String)](M_Tessa_Platform_NotificationObject_OnPropertyChanged_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(PropertyChangedEventArgs,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync.htm)|
Уведомляет об изменении свойства с именем, заданным в аргументах события,
асинхронно, в соответствии с принятым для текущего объекта поведением. Если
есть возможность вызвать событие синхронно, то оно вызывается синхронно. Если
объект является моделью представления WPF и текущий поток отличен от потока
диспетчера WPF для приложения (основной поток UI), то выполнение асинхронно
переключается в этот поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[OnPropertyChangedAsync(String,
Boolean)](M_Tessa_Platform_NotificationObject_OnPropertyChangedAsync_1.htm)|
Уведомляет об изменении свойства с заданным именем у объекта асинхронно, в
соответствии с принятым для текущего объекта поведением. Если есть возможность
вызвать событие синхронно, то оно вызывается синхронно. Если объект является
моделью представления WPF и текущий поток отличен от потока диспетчера WPF для
приложения (основной поток UI), то выполнение асинхронно переключается в этот
поток. Если это не так, то событие выполняется синхронно.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
[SetStateAsync](M_Tessa_Files_FileSignatureData_SetStateAsync.htm)|
Устанавливает состояние бинарных данных файла подписи.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[PropertyChanged](E_Tessa_Platform_NotificationObject_PropertyChanged.htm)|
Событие, уведомляющее об изменении свойства с определённым именем у модели
представления.  
(Унаследован от [NotificationObject](T_Tessa_Platform_NotificationObject.htm))  
---|---  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetNullableBytesAsync](M_Tessa_Files_FileExtensions_GetNullableBytesAsync.htm)|
Возвращает бинарные данные подписи файла в виде массива байт или null, если
бинарные данные отсутствуют или ещё не загружены.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
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
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
