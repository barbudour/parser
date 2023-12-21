# IErrorLog - интерфейс
Описание интерфейса глобального лога ошибок
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IErrorLog : INotifyPropertyChanged
VB __Копировать
     Public Interface IErrorLog
    	Inherits INotifyPropertyChanged
C++ __Копировать
     public interface class IErrorLog : INotifyPropertyChanged
F# __Копировать
     type IErrorLog = 
        interface
            interface INotifyPropertyChanged
        end
Implements
    [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
##  __Свойства
[Errors](P_Tessa_Applications_IErrorLog_Errors.htm)|  Gets Ошибки  
---|---  
[HasErrors](P_Tessa_Applications_IErrorLog_HasErrors.htm)|  Gets a value
indicating whether Признак наличия ошибок  
## __Методы
[Clear](M_Tessa_Applications_IErrorLog_Clear.htm)|  Очищает лог  
---|---  
[Execute](M_Tessa_Applications_IErrorLog_Execute.htm)|  Выполняет действие
validationAction для добавления ошибки в лог  
## __События
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
