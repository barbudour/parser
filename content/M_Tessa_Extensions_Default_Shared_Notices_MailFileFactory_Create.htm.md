# MailFileFactory.Create(String, Byte[]) - метод
Создаёт файл, который может прикладываться к письму и данные которого встроены
в структуру объекта [MailFile](T_Tessa_Notices_MailFile.htm). Рекомендуется
использовать только для небольших файлов (желательно не более 100 Кб).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Notices](N_Tessa_Extensions_Default_Shared_Notices.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static MailFile Create(
    	string fileName,
    	byte[] data
    )
VB __Копировать
     Public Shared Function Create ( 
    	fileName As String,
    	data As Byte()
    ) As MailFile
C++ __Копировать
     public:
    static MailFile^ Create(
    	String^ fileName, 
    	array<unsigned char>^ data
    )
F# __Копировать
     static member Create : 
            fileName : string * 
            data : byte[] -> MailFile 
#### Параметры
fileName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя прикладываемого файла.
data [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
    Данные прикладываемого файла.
#### Возвращаемое значение
[MailFile](T_Tessa_Notices_MailFile.htm)  
Файл, приложенный к письму.
##  __См. также
#### Ссылки
[MailFileFactory -
](T_Tessa_Extensions_Default_Shared_Notices_MailFileFactory.htm)
[Create -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Notices_MailFileFactory_Create.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
