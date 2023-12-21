# IFileSignatureData - интерфейс
Объект, содержащий информацию по бинарным данным файла подписи.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileSignatureData : INotifyPropertyChanged
VB __Копировать
     Public Interface IFileSignatureData
    	Inherits INotifyPropertyChanged
C++ __Копировать
     public interface class IFileSignatureData : INotifyPropertyChanged
F# __Копировать
     type IFileSignatureData = 
        interface
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
##  __Свойства
[IsEmpty](P_Tessa_Files_IFileSignatureData_IsEmpty.htm)| Признак того, что
бинарные данные файла подписи не заполнены.  
---|---  
[State](P_Tessa_Files_IFileSignatureData_State.htm)| Состояние бинарных данных
файла подписи.  
##  __Методы
[GetBytesAsync](M_Tessa_Files_IFileSignatureData_GetBytesAsync.htm)|
Возвращает бинарные данные файла подписи в виде массива байт. Возвращённый
массив не равенnull.  
---|---  
[SetStateAsync](M_Tessa_Files_IFileSignatureData_SetStateAsync.htm)|
Устанавливает состояние бинарных данных файла подписи.  
##  __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __Методы расширения
[GetNullableBytesAsync](M_Tessa_Files_FileExtensions_GetNullableBytesAsync.htm)|
Возвращает бинарные данные подписи файла в виде массива байт или null, если
бинарные данные отсутствуют или ещё не загружены.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
