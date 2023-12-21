# CardTaskDialogHelper.GetFileVersionFromInfo - метод
Возвращает информацию о версии файла диалога с временем жизни "Запрос"
([Info](T_Tessa_Cards_CardTaskDialogStoreMode.htm)).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardFileVersion? GetFileVersionFromInfo(
    	CardInfoStorageObject infoStorageObject
    )
VB __Копировать
     Public Shared Function GetFileVersionFromInfo ( 
    	infoStorageObject As CardInfoStorageObject
    ) As CardFileVersion
C++ __Копировать
     public:
    static CardFileVersion^ GetFileVersionFromInfo(
    	CardInfoStorageObject^ infoStorageObject
    )
F# __Копировать
     static member GetFileVersionFromInfo : 
            infoStorageObject : CardInfoStorageObject -> CardFileVersion 
#### Параметры
infoStorageObject
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Объект, содержащий получаемую информацию.
#### Возвращаемое значение
[CardFileVersion](T_Tessa_Cards_CardFileVersion.htm)  
Информация о версии файла или значение по умолчанию для типа, если её не
удалось получить.
##  __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
