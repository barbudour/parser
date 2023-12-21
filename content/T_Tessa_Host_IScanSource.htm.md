# IScanSource - интерфейс
Информация по источнику сканирования, обычно соответствует драйверу
сканирования.
## __Definition
 **Пространство имён:** [Tessa.Host](N_Tessa_Host.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IScanSource : IEquatable<IScanSource>
VB __Копировать
     Public Interface IScanSource
    	Inherits IEquatable(Of IScanSource)
C++ __Копировать
     public interface class IScanSource : IEquatable<IScanSource^>
F# __Копировать
     type IScanSource = 
        interface
            interface IEquatable<IScanSource>
        end
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IScanSource>
##  __Свойства
[DriverVersion](P_Tessa_Host_IScanSource_DriverVersion.htm)|  Версия драйвера
для сканера.  
---|---  
[ID](P_Tessa_Host_IScanSource_ID.htm)|  Идентификатор источника  
[Name](P_Tessa_Host_IScanSource_Name.htm)|  Имя драйвера для сканера.  
[ProtocolVersion](P_Tessa_Host_IScanSource_ProtocolVersion.htm)|  Версия
протокола TWAIN/WIA для сканера.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.iequatable-1.equals#system-
iequatable-1-equals\(-0\))| Indicates whether the current object is equal to
another object of the same type.  
(Унаследован от
[IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<IScanSource>)  
---|---  
##  __См. также
#### Ссылки
[Tessa.Host - пространство имён](N_Tessa_Host.htm)
