# IFileConverterOutputFormatPolicy - интерфейс
Политика, определяющая допустимость выходного формата по конвертации файлов.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileConverterOutputFormatPolicy : IExtensionPolicy
VB __Копировать
     Public Interface IFileConverterOutputFormatPolicy
    	Inherits IExtensionPolicy
C++ __Копировать
     public interface class IFileConverterOutputFormatPolicy : IExtensionPolicy
F# __Копировать
     type IFileConverterOutputFormatPolicy = 
        interface
            interface IExtensionPolicy
        end
Implements
    [IExtensionPolicy](T_Tessa_Extensions_IExtensionPolicy.htm)
##  __Свойства
[IsAllowAny](P_Tessa_FileConverters_IFileConverterOutputFormatPolicy_IsAllowAny.htm)|
Признак того, что политика разрешает любые выходные форматы файлов, в том
числе неизвестные на момент фильтрации.  
---|---  
##  __Методы
[IsAllowed](M_Tessa_FileConverters_IFileConverterOutputFormatPolicy_IsAllowed.htm)|
Возвращает признак того, что выполнение методов расширения допустимо для
заданного выходного формата по конвертации файлов.  
---|---  
##  __См. также
#### Ссылки
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
