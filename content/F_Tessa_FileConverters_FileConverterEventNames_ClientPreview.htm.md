# FileConverterEventNames.ClientPreview - поле
Предпросмотр из web-клиента или desktop-клиента.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public const string ClientPreview = "ClientPreview"
VB __Копировать
     Public Const ClientPreview As String = "ClientPreview"
C++ __Копировать
     public:
    literal String^ ClientPreview = "ClientPreview"
F# __Копировать
     static val mutable ClientPreview: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Для web-клиента и desktop-клиента используется одно и то же имя события, чтобы
при одновременном предпросмотре из web-клиента и desktop-клиента конвертация
не выполнялась дважды. В этом случае создаётся операция в клиенте, который
первый запросил конвертацию, а второй клиент ожидает ту же операцию, но не
создаёт операцию дважды.
## __См. также
#### Ссылки
[FileConverterEventNames -
](T_Tessa_FileConverters_FileConverterEventNames.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
