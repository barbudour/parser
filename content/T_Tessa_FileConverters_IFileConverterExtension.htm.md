# IFileConverterExtension - интерфейс
Расширение для операции по конвертированию файла.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileConverterExtension : IExtension
VB __Копировать
     Public Interface IFileConverterExtension
    	Inherits IExtension
C++ __Копировать
     public interface class IFileConverterExtension : IExtension
F# __Копировать
     type IFileConverterExtension = 
        interface
            interface IExtension
        end
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[AfterRequest](M_Tessa_FileConverters_IFileConverterExtension_AfterRequest.htm)|
Метод, выполняемый после конвертирования файлов, причём как в случае успеха,
так и при возникновении ошибок. Проверить успешность операции можно по
свойству context.RequestIsSuccessful. Файл после конвертации доступен в этом
методе по заданному в контексте пути. Если метод вернёт ошибку в результате
валидации или выбросит исключение, то результаты конвертации не будут
сохранены.  
---|---  
[BeforeRequest](M_Tessa_FileConverters_IFileConverterExtension_BeforeRequest.htm)|
Метод, выполняемый перед конвертированием файлов. Файл после конвертации
недоступен в этом методе. Если метод вернёт ошибку в результате валидации или
выбросит исключение, то конвертация не будет выполнена.  
## __См. также
#### Ссылки
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
