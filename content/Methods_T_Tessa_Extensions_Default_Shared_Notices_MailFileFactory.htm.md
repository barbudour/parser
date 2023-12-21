# MailFileFactory - методы
##  __Методы
[Create(String,
Byte[])](M_Tessa_Extensions_Default_Shared_Notices_MailFileFactory_Create.htm)|
Создаёт файл, который может прикладываться к письму и данные которого встроены
в структуру объекта [MailFile](T_Tessa_Notices_MailFile.htm). Рекомендуется
использовать только для небольших файлов (желательно не более 100 Кб).  
---|---  
[Create(String, String,
Encoding)](M_Tessa_Extensions_Default_Shared_Notices_MailFileFactory_Create_1.htm)|
Создаёт файл, который может прикладываться к письму и текстовые данные
которого встроены в структуру объекта [MailFile](T_Tessa_Notices_MailFile.htm)
в кодировке encoding. Рекомендуется использовать только для небольших файлов
(желательно не более 100 Кб).  
[CreateFromServerPath](M_Tessa_Extensions_Default_Shared_Notices_MailFileFactory_CreateFromServerPath.htm)|
Создаёт файл, который может прикладываться к письму и который доступен по
заданному пути на сервере, на котором установлен Chronos. После успешной
отправки файл может быть удалён в зависимости от настройки
[MailFileRemovalType](T_Tessa_Extensions_Default_Shared_Notices_MailFileRemovalType.htm).  
## __См. также
#### Ссылки
[MailFileFactory -
](T_Tessa_Extensions_Default_Shared_Notices_MailFileFactory.htm)
[Tessa.Extensions.Default.Shared.Notices - пространство
имён](N_Tessa_Extensions_Default_Shared_Notices.htm)
